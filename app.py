"""
PlantCare AI - Flask Application & REST API
Integrates Computer Vision (OpenCV), Deep Learning (TensorFlow CNN),
SQLite Scan History, and AI Agricultural Farming Assistant.
"""

import os
import uuid
import base64
from datetime import datetime
from flask import Flask, request, jsonify, render_template, send_from_directory
from werkzeug.utils import secure_filename

import database
from model_engine import get_model_engine
from disease_data import DISEASE_DATABASE, get_disease_info
from assistant import assistant_engine

app = Flask(__name__)
app.config['SECRET_KEY'] = 'plantcare-ai-secure-secret-key-2026'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max upload

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'static', 'uploads')
SAMPLE_DIR = os.path.join(BASE_DIR, 'static', 'images', 'samples')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(os.path.join(UPLOAD_DIR, 'processed'), exist_ok=True)

# Initialize SQLite database
database.init_db()

# Pre-warm TensorFlow model engine
model_engine = get_model_engine()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    """Main Web Application Dashboard."""
    return render_template('index.html')

@app.route('/api/model-info', methods=['GET'])
def get_model_info():
    """Return model status and framework details."""
    return jsonify({
        "status": "online",
        "engine": "TensorFlow CNN",
        "framework_version": "TensorFlow 2.21.0 + OpenCV 5.0.0",
        "mode_status": model_engine.mode_status,
        "is_trained_weights": model_engine.is_trained_weights,
        "classes_supported": len(model_engine.class_names),
        "input_dimensions": "224x224x3 RGB",
        "database": "SQLite 3"
    })

@app.route('/api/samples', methods=['GET'])
def get_sample_leaves():
    """Return available sample leaf images for instant 1-click testing."""
    samples = [
        {
            "id": "tomato_early_blight",
            "name": "Tomato Early Blight",
            "crop": "Tomato",
            "filename": "tomato_early_blight_sample.jpg",
            "thumbnail": "/static/images/samples/tomato_early_blight_sample.jpg",
            "description": "Bullseye target spots with concentric rings and yellow halo."
        },
        {
            "id": "tomato_late_blight",
            "name": "Tomato Late Blight",
            "crop": "Tomato",
            "filename": "tomato_late_blight_sample.jpg",
            "thumbnail": "/static/images/samples/tomato_late_blight_sample.jpg",
            "description": "Water-soaked dark necrotic blotches with grayish border."
        },
        {
            "id": "tomato_healthy",
            "name": "Tomato Healthy",
            "crop": "Tomato",
            "filename": "tomato_healthy_sample.jpg",
            "thumbnail": "/static/images/samples/tomato_healthy_sample.jpg",
            "description": "Vibrant emerald green foliage without lesions or chlorosis."
        },
        {
            "id": "potato_early_blight",
            "name": "Potato Early Blight",
            "crop": "Potato",
            "filename": "potato_early_blight_sample.jpg",
            "thumbnail": "/static/images/samples/potato_early_blight_sample.jpg",
            "description": "Brown circular spots with chlorotic margin."
        },
        {
            "id": "apple_scab",
            "name": "Apple Scab",
            "crop": "Apple",
            "filename": "apple_scab_sample.jpg",
            "thumbnail": "/static/images/samples/apple_scab_sample.jpg",
            "description": "Velvety olive-green to black corky scab lesions."
        }
    ]
    return jsonify(samples)

@app.route('/api/predict', methods=['POST'])
def predict_disease():
    """
    Handle plant leaf image upload (File or Base64 Webcam/Preset),
    run OpenCV preprocessing and TensorFlow CNN inference,
    fetch treatment recommendations, and log to SQLite.
    """
    try:
        user_crop_hint = request.form.get('crop_hint') or (request.json and request.json.get('crop_hint'))
        saved_filename = None
        saved_filepath = None
        original_display_name = "Leaf Scan"

        # Case 1: Standard file upload
        if 'image' in request.files and request.files['image'].filename != '':
            file = request.files['image']
            if not allowed_file(file.filename):
                return jsonify({"error": "Unsupported file format. Please upload JPG, PNG, or WEBP."}), 400

            original_display_name = secure_filename(file.filename)
            ext = original_display_name.rsplit('.', 1)[1].lower()
            saved_filename = f"leaf_{uuid.uuid4().hex[:10]}_{int(datetime.now().timestamp())}.{ext}"
            saved_filepath = os.path.join(UPLOAD_DIR, saved_filename)
            file.save(saved_filepath)

        # Case 2: Base64 string (webcam snapshot or preset sample clone)
        elif request.is_json and 'image_base64' in request.json:
            b64_data = request.json['image_base64']
            if ',' in b64_data:
                b64_data = b64_data.split(',', 1)[1]
            img_bytes = base64.b64decode(b64_data)
            saved_filename = f"cam_{uuid.uuid4().hex[:10]}_{int(datetime.now().timestamp())}.jpg"
            saved_filepath = os.path.join(UPLOAD_DIR, saved_filename)
            with open(saved_filepath, 'wb') as f:
                f.write(img_bytes)
            original_display_name = request.json.get('original_name', 'Live Camera Snapshot')

        # Case 3: Picked a pre-generated sample leaf
        elif request.is_json and 'sample_filename' in request.json:
            sample_name = request.json['sample_filename']
            sample_src = os.path.join(SAMPLE_DIR, secure_filename(sample_name))
            if not os.path.exists(sample_src):
                return jsonify({"error": "Sample file not found."}), 404

            ext = sample_name.rsplit('.', 1)[1].lower()
            saved_filename = f"sample_{uuid.uuid4().hex[:8]}_{int(datetime.now().timestamp())}.{ext}"
            saved_filepath = os.path.join(UPLOAD_DIR, saved_filename)
            with open(sample_src, 'rb') as src_f, open(saved_filepath, 'wb') as dst_f:
                dst_f.write(src_f.read())
            original_display_name = sample_name.replace("_", " ").title()

        else:
            return jsonify({"error": "No image file, sample, or camera snapshot received."}), 400

        # Execute OpenCV Preprocessing + TensorFlow CNN inference
        prediction_result = model_engine.predict(saved_filepath, user_crop_hint=user_crop_hint)

        # Retrieve comprehensive agricultural treatment guidelines
        disease_info = get_disease_info(prediction_result['class_id'])

        # Relative web paths
        image_url = f"/static/uploads/{saved_filename}"
        mask_filename = os.path.basename(prediction_result['mask_path'])
        mask_url = f"/static/uploads/processed/{mask_filename}"

        # Persist diagnostic record to SQLite database
        scan_id = database.save_scan(
            filename=saved_filename,
            original_name=original_display_name,
            crop=prediction_result['crop'],
            disease_name=prediction_result['disease_name'],
            disease_id=prediction_result['class_id'],
            pathogen=disease_info.get('pathogen', 'N/A'),
            confidence=prediction_result['confidence_percentage'],
            severity=disease_info.get('severity', 'Moderate'),
            processed_mask_path=mask_url,
            notes=f"Detected with {prediction_result['num_lesions_detected']} lesion contours; Foliage ratio {prediction_result['foliage_ratio']}%"
        )

        response_data = {
            "success": True,
            "scan_id": scan_id,
            "crop": prediction_result['crop'],
            "disease_name": prediction_result['disease_name'],
            "class_id": prediction_result['class_id'],
            "pathogen": disease_info.get('pathogen', 'Unknown'),
            "severity": disease_info.get('severity', 'Moderate'),
            "severity_color": disease_info.get('severity_color', 'warning'),
            "confidence_percentage": prediction_result['confidence_percentage'],
            "model_mode": prediction_result['model_mode'],
            "is_trained_weights": prediction_result['is_trained_weights'],
            "is_likely_plant": prediction_result['is_likely_plant'],
            "image_url": image_url,
            "mask_url": mask_url,
            "foliage_ratio": prediction_result['foliage_ratio'],
            "lesion_ratio": prediction_result['lesion_ratio'],
            "num_lesions_detected": prediction_result['num_lesions_detected'],
            "top_3_predictions": prediction_result['top_3_predictions'],
            "treatment": {
                "overview": disease_info.get('overview', ''),
                "symptoms": disease_info.get('symptoms', []),
                "causes": disease_info.get('causes', []),
                "treatment_chemical": disease_info.get('treatment_chemical', []),
                "treatment_organic": disease_info.get('treatment_organic', []),
                "prevention": disease_info.get('prevention', [])
            }
        }
        return jsonify(response_data)

    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({"error": f"Diagnostic processing failed: {str(e)}"}), 500

@app.route('/api/chat', methods=['POST'])
def chat_assistant():
    """
    AI Farming Assistant Chatbot Endpoint.
    Responds to agricultural questions, remedies, irrigation, and context scans.
    """
    try:
        data = request.get_json() or {}
        message = data.get('message', '').strip()
        session_id = data.get('session_id', 'farmer-session-1')
        context_scan = data.get('context_scan', None)

        if not message:
            return jsonify({"error": "Empty message."}), 400

        # Save user query to chat log
        database.save_chat_message(session_id, "farmer", message)

        # Generate expert agricultural response
        response_dict = assistant_engine.respond(message, context_scan=context_scan)

        # Save assistant response
        database.save_chat_message(session_id, "assistant", response_dict['reply'])

        return jsonify({
            "success": True,
            "reply": response_dict['reply'],
            "suggested_questions": response_dict.get('suggested_questions', [])
        })

    except Exception as e:
        return jsonify({"error": f"Assistant error: {str(e)}"}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Return scan history from SQLite database."""
    scans = database.get_all_scans(limit=100)
    stats = database.get_db_stats()
    return jsonify({
        "scans": scans,
        "stats": stats
    })

@app.route('/api/history/<int:scan_id>', methods=['GET'])
def get_single_history(scan_id):
    """Retrieve full details of a single scan."""
    scan = database.get_scan(scan_id)
    if not scan:
        return jsonify({"error": "Scan record not found"}), 404
    
    disease_info = get_disease_info(scan.get('disease_id', ''))
    return jsonify({
        "scan": scan,
        "treatment": disease_info
    })

@app.route('/api/history/<int:scan_id>', methods=['DELETE'])
def delete_history_item(scan_id):
    """Delete a scan item from SQLite."""
    success = database.delete_scan(scan_id)
    return jsonify({"success": success})

@app.route('/api/history/clear', methods=['POST'])
def clear_history():
    """Clear all scans from SQLite database."""
    database.clear_all_scans()
    return jsonify({"success": True})

@app.route('/api/disease-library', methods=['GET'])
def get_disease_library():
    """Return all diseases in the knowledge base for reference."""
    library = []
    for key, val in DISEASE_DATABASE.items():
        library.append(val)
    return jsonify(library)

@app.route('/api/stats', methods=['GET'])
def get_quick_stats():
    """Return SQLite scan stats."""
    return jsonify(database.get_db_stats())

if __name__ == '__main__':
    print("=" * 60)
    print(" Starting PlantCare AI Server on http://127.0.0.1:5000")
    print("=" * 60)
    app.run(host='127.0.0.1', port=5000, debug=True)
