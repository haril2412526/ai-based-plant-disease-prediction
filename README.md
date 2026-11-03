# PlantCare AI — Modern Plant Disease Detection & Farming Advisory

A modern, professional, fully functional AI-based web application that detects plant diseases from leaf photographs, provides scientific conventional and organic treatment recommendations, features a 24/7 AI Farming Assistant chatbot, and logs scan history using SQLite.

---

## 🌟 Key Features

### 1. Home Page & Dashboard
- **Modern Agriculture-Themed UI:** Emerald forest green, leaf accents, crisp typography, smooth transitions, and glassmorphism.
- **Hero & Interactive Demonstrator:** Live system metrics, animated scan laser, and 1-click test specimens.
- **Workflow Highlights:** Visual 3-step guide explaining leaf upload, computer vision segmentation, and AI diagnostics.

### 2. Plant Disease Detection Engine
- **Deep Learning CNN (TensorFlow):** Multi-layer Convolutional Neural Network trained on multi-scale spatial leaf patterns (17 classes supported).
- **OpenCV Image Processing:**
  - Automated chlorophyll index verification (flags non-plant inputs).
  - Dual visualizer: Toggle between **Original Leaf Specimen** and **OpenCV Lesion Segmentation Mask** (showing red contour-mapped necrotic spots).
  - Surface lesion ratio (%) and spot count analysis.
- **Multiple Input Modes:**
  - Drag & drop or file browse (JPG, PNG, WEBP).
  - Live webcam camera capture with target crosshairs.
  - 1-click preset leaf specimens for immediate evaluation.
- **Diagnostic Metrics:** Disease name, scientific pathogen, severity level badge, exact AI confidence score, and top-3 probability breakdown.

### 3. AI Treatment & Prevention Recommendations
- **Organic & Biological Options:** OMRI-listed treatments, cold-pressed neem oil formulations, *Bacillus subtilis* bio-fungicides, copper soaps, and compost teas.
- **Conventional / Chemical Recommendations:** Targeted fungicides/bactericides, dosage guidelines, application windows, and pre-harvest intervals (PHI).
- **Symptoms & Causes:** Bullseye concentric rings, water-soaked lesions, spore propagation, and environmental humidity triggers.
- **Cultural & Preventative Practices:** 3-year crop rotations, drip irrigation guidelines, pruning canopy airflow, and sanitization protocols.
- **Print / Export Report:** Print-ready formatting for grower records.

### 4. AI Farming Assistant (Chatbot)
- **Interactive Conversational UI:** Context-aware advisory answering questions on crop health, soil pH, fertilizers (NPK ratios), pest control, and watering schedules.
- **Active Scan Integration:** Automatically references the most recently diagnosed leaf condition.
- **Dynamic Quick Prompts:** Suggests intelligent follow-up inquiries.
- **Voice Text-to-Speech:** Built-in Web Speech API speaker button to read agricultural solutions aloud.

### 5. Scan History (SQLite Database)
- **Persistent Storage:** Saves image filename, original name, crop, detected disease, pathogen, confidence, severity, and timestamp into `plantcare.db`.
- **Interactive Search & Filtering:** Filter by crop family (Tomato, Potato, Apple, Corn, Grape, Pepper) and severity level.
- **Detailed Inspection Modal:** View saved leaf thumbnail alongside OpenCV lesion masks and full treatment instructions.
- **Summary Counters:** Total scans, healthy leaves, disease cases, and most frequent diagnosis.

---

## 🏗️ Architecture & Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | HTML5, CSS3 (Custom Responsive Agriculture Design), JavaScript (ES6+), FontAwesome Icons, Plus Jakarta Sans & Outfit fonts |
| **Backend** | Python Flask (RESTful API, asynchronous routing) |
| **Artificial Intelligence** | TensorFlow & Keras (Convolutional Neural Network) |
| **Computer Vision** | OpenCV (`cv2`) for leaf detection, HSV color space masking, and lesion contour drawing |
| **Database** | SQLite 3 (`plantcare.db`) |

---

## 📁 Project Structure

```
ai project/
├── app.py                      # Flask REST API server
├── model_engine.py             # TensorFlow CNN model & OpenCV preprocessing pipeline
├── disease_data.py             # Knowledge base of 17 crop diseases & treatments
├── assistant.py                # AI Farming Assistant advisory engine
├── database.py                 # SQLite database models and helper functions
├── create_sample_leaves.py     # Script to generate sample leaf specimens
├── test_app.py                 # Automated end-to-end verification test suite
├── requirements.txt            # Python dependencies
├── run_plantcare.bat           # 1-click Windows startup batch script
├── templates/
│   └── index.html              # Main web application dashboard
└── static/
    ├── css/
    │   └── style.css           # Modern agricultural CSS theme
    ├── js/
    │   ├── app.js              # Core UI controller & detector logic
    │   ├── chat.js             # Chatbot controller with voice synthesis
    │   └── history.js          # SQLite history management & filters
    ├── images/
    │   └── samples/            # Pre-calibrated leaf samples for 1-click tests
    └── uploads/                # User uploaded leaf images & OpenCV masks
```

---

## 🚀 Quick Start Guide

### 1. Requirements
- Python 3.9, 3.10, or 3.11
- Modern web browser (Chrome, Edge, Firefox, Safari)

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Start the Web Server
Run the Flask server:
```bash
python app.py
```
Or double-click `run_plantcare.bat` on Windows.

### 4. Open in Browser
Navigate to:
```
http://127.0.0.1:5000
```

---

## 🧪 Running the Test Suite

To verify all endpoints, CNN prediction, OpenCV segmentation, SQLite persistence, and chatbot functionality:
```bash
python test_app.py
```
All 9 automated test suites validate end-to-end functionality.
