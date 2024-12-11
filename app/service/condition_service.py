from app.dao.database import get_db


def get_all_conditions():
    """Retrieve all unique medical conditions from the database."""
    db = get_db()
    conditions = db.conditions.distinct("code")
    return [{"condition_code": condition} for condition in conditions]
