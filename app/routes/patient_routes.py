from flask import Blueprint, request, jsonify
from app.service.patient_service import find_patients_with_conditions

bp = Blueprint('patient_routes', __name__)


@bp.route('/chronic-diseases', methods=['POST'])
def get_patients_with_chronic_diseases():
    """
    API endpoint to find patients with chronic diseases based on:
    - Doctor ID
    - List of conditions
    """
    data = request.get_json()
    doctor_id = data.get("doctor_id")
    conditions = data.get("conditions", [])

    if not doctor_id or not conditions:
        return jsonify({"error": "doctor_id and conditions are required"}), 400

    patients = find_patients_with_conditions(doctor_id, conditions)
    return jsonify(patients), 200