"""
End-to-End Test Suite for PlantCare AI
Tests all routes, model engine, OpenCV preprocessing, SQLite persistence, and chatbot assistant.
"""

import sys
import os
import json
import io

# Force UTF-8 on Windows stdout if possible
if sys.stdout.encoding and sys.stdout.encoding.lower() != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from app import app
import database

def run_tests():
    print("=" * 60)
    print(" Running PlantCare AI Automated Test Suite")
    print("=" * 60)

    client = app.test_client()

    # 1. Test Home page
    print("\n[1] Testing GET / ...")
    res = client.get('/')
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    assert b"PlantCare" in res.data
    print(" [OK] Home page loaded successfully (HTTP 200).")

    # 2. Test Model Info API
    print("\n[2] Testing GET /api/model-info ...")
    res = client.get('/api/model-info')
    assert res.status_code == 200
    data = res.get_json()
    assert data["status"] == "online"
    assert "TensorFlow" in data["engine"]
    assert data["classes_supported"] == 17
    print(f" [OK] Model info valid: {data['engine']}, {data['classes_supported']} classes.")

    # 3. Test Samples API
    print("\n[3] Testing GET /api/samples ...")
    res = client.get('/api/samples')
    assert res.status_code == 200
    samples = res.get_json()
    assert len(samples) >= 5
    print(f" [OK] Retrieved {len(samples)} pre-calibrated sample leaves.")

    # 4. Test Predict API using preset sample
    print("\n[4] Testing POST /api/predict (Preset Sample) ...")
    res = client.post('/api/predict', 
                      json={'sample_filename': 'tomato_early_blight_sample.jpg', 'crop_hint': 'Tomato'},
                      content_type='application/json')
    assert res.status_code == 200, f"Expected 200, got {res.status_code}: {res.data}"
    pred = res.get_json()
    assert pred["success"] is True
    assert pred["crop"] == "Tomato"
    assert "Early blight" in pred["disease_name"]
    assert "Alternaria solani" in pred["pathogen"]
    assert pred["confidence_percentage"] > 70
    assert len(pred["treatment"]["treatment_organic"]) > 0
    assert len(pred["treatment"]["treatment_chemical"]) > 0
    assert "mask_url" in pred
    print(f" [OK] Diagnosis Succeeded: {pred['crop']} {pred['disease_name']} ({pred['confidence_percentage']}%)")
    print(f"      Pathogen: {pred['pathogen']}")
    print(f"      Lesions Detected: {pred['num_lesions_detected']}, Foliage: {pred['foliage_ratio']}%")
    print(f"      Organic Treatment: {pred['treatment']['treatment_organic'][0]}")

    # 5. Test Predict API using file upload
    print("\n[5] Testing POST /api/predict (Multipart File Upload) ...")
    sample_file_path = os.path.join('static', 'images', 'samples', 'potato_early_blight_sample.jpg')
    with open(sample_file_path, 'rb') as f:
        file_bytes = f.read()
    
    res = client.post('/api/predict',
                      data={'image': (io.BytesIO(file_bytes), 'potato_early_blight_sample.jpg'), 'crop_hint': 'Potato'},
                      content_type='multipart/form-data')
    assert res.status_code == 200
    pred2 = res.get_json()
    assert pred2["success"] is True
    assert pred2["crop"] == "Potato"
    print(f" [OK] File upload diagnosis: {pred2['crop']} {pred2['disease_name']} ({pred2['confidence_percentage']}%)")

    # 6. Test History API
    print("\n[6] Testing GET /api/history (SQLite records) ...")
    res = client.get('/api/history')
    assert res.status_code == 200
    hist = res.get_json()
    assert len(hist["scans"]) >= 2
    assert hist["stats"]["total_scans"] >= 2
    print(f" [OK] SQLite History verified: {len(hist['scans'])} scans persisted. Total stats: {hist['stats']}")

    # 7. Test AI Farming Assistant Chatbot
    print("\n[7] Testing POST /api/chat (Assistant) ...")
    res = client.post('/api/chat',
                      json={
                          'message': 'How do I prepare neem oil spray for tomato early blight?',
                          'session_id': 'test-session',
                          'context_scan': pred
                      },
                      content_type='application/json')
    assert res.status_code == 200
    chat_res = res.get_json()
    assert chat_res["success"] is True
    assert "Neem" in chat_res["reply"] or "Tomato" in chat_res["reply"]
    print(f" [OK] Assistant reply received ({len(chat_res['reply'])} chars).")
    print(f"      Suggested follow-ups: {chat_res['suggested_questions']}")

    # 8. Test Disease Library API
    print("\n[8] Testing GET /api/disease-library ...")
    res = client.get('/api/disease-library')
    assert res.status_code == 200
    lib = res.get_json()
    assert len(lib) >= 15
    print(f" [OK] Disease Library verified: {len(lib)} diseases cataloged.")

    # 9. Test Delete History Item
    first_id = hist["scans"][0]["id"]
    print(f"\n[9] Testing DELETE /api/history/{first_id} ...")
    res = client.delete(f'/api/history/{first_id}')
    assert res.status_code == 200
    print(" [OK] Successfully deleted scan from SQLite.")

    print("\n" + "=" * 60)
    print(" ALL 9 TEST SUITES PASSED FLAWLESSLY! [OK]")
    print("=" * 60)

if __name__ == '__main__':
    run_tests()
