from flask import Blueprint, jsonify
from app.service.doctor_service import get_all_doctors

bp = Blueprint('doctor_routes', __name__)


@bp.route('/', methods=['GET'])
def list_all_doctors():
    doctors = get_all_doctors()
    return jsonify(doctors), 200
