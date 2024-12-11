from flask import Blueprint, jsonify
from app.service.condition_service import get_all_conditions

bp = Blueprint('condition_routes', __name__)


@bp.route('/', methods=['GET'])
def list_conditions():
    conditions = get_all_conditions()
    return jsonify(conditions), 200
