"""
PlantCare AI - SQLite Database Interface
Stores and manages plant disease scan history, diagnostics, and farmer inquiries.
"""

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plantcare.db')

def get_connection():
    """Create and return a database connection with dict-like row factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database tables with indexes."""
    with get_connection() as conn:
        cursor = conn.cursor()
        
        # Scans table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                filename TEXT NOT NULL,
                original_name TEXT,
                crop TEXT NOT NULL,
                disease_name TEXT NOT NULL,
                disease_id TEXT NOT NULL,
                pathogen TEXT,
                confidence REAL NOT NULL,
                severity TEXT NOT NULL,
                processed_mask_path TEXT,
                notes TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        # Assistant Chat logs table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS chat_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                session_id TEXT,
                sender TEXT NOT NULL,
                message TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        
        conn.commit()

def save_scan(filename: str, original_name: str, crop: str, disease_name: str,
              disease_id: str, pathogen: str, confidence: float, severity: str,
              processed_mask_path: str = None, notes: str = None) -> int:
    """Save a new leaf scan result into SQLite."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO scans (
                filename, original_name, crop, disease_name, disease_id,
                pathogen, confidence, severity, processed_mask_path, notes, created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            filename,
            original_name or filename,
            crop,
            disease_name,
            disease_id,
            pathogen,
            confidence,
            severity,
            processed_mask_path,
            notes,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))
        conn.commit()
        return cursor.lastrowid

def get_all_scans(limit: int = 100):
    """Retrieve scan history ordered by newest first."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, filename, original_name, crop, disease_name, disease_id,
                   pathogen, confidence, severity, processed_mask_path, notes, created_at
            FROM scans
            ORDER BY id DESC
            LIMIT ?
        ''', (limit,))
        rows = cursor.fetchall()
        return [dict(row) for row in rows]

def get_scan(scan_id: int):
    """Retrieve single scan by ID."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM scans WHERE id = ?
        ''', (scan_id,))
        row = cursor.fetchone()
        return dict(row) if row else None

def delete_scan(scan_id: int) -> bool:
    """Delete a scan record from the database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM scans WHERE id = ?', (scan_id,))
        conn.commit()
        return cursor.rowcount > 0

def clear_all_scans():
    """Clear all scans from database."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('DELETE FROM scans')
        conn.commit()

def get_db_stats():
    """Return summary statistics of scan history."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) as total FROM scans')
        total = cursor.fetchone()['total']
        
        cursor.execute("SELECT COUNT(*) as healthy FROM scans WHERE disease_name LIKE '%Healthy%'")
        healthy = cursor.fetchone()['healthy']
        
        diseased = total - healthy
        
        # Most frequent crop/disease
        cursor.execute('''
            SELECT disease_name, COUNT(*) as cnt 
            FROM scans 
            GROUP BY disease_name 
            ORDER BY cnt DESC 
            LIMIT 1
        ''')
        top_disease = cursor.fetchone()
        top_name = top_disease['disease_name'] if top_disease else "None yet"
        
        return {
            "total_scans": total,
            "healthy_count": healthy,
            "diseased_count": diseased,
            "top_disease": top_name
        }

def save_chat_message(session_id: str, sender: str, message: str):
    """Log an interaction from the AI Farming Assistant."""
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO chat_logs (session_id, sender, message, created_at)
            VALUES (?, ?, ?, ?)
        ''', (session_id, sender, message, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        conn.commit()

if __name__ == '__main__':
    init_db()
    print("Database initialized successfully at", DB_PATH)
