from flask import Blueprint
from app.routes.doctor_routes import bp as doctor_bp
from app.routes.condition_routes import bp as condition_bp
from app.routes.patient_routes import bp as patient_bp

bp = Blueprint('api', __name__)
bp.register_blueprint(doctor_bp, url_prefix='/doctors')
bp.register_blueprint(condition_bp, url_prefix='/conditions')
bp.register_blueprint(patient_bp, url_prefix='/patients')
