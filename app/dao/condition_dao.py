from .database import get_db

db = get_db()


def save_conditions(conditions):
    db.conditions.insert_many(conditions)


def save_conditions_upsert(conditions):
    """
    Save conditions to the database, ensuring no duplicates are inserted.
    """
    for condition in conditions:
        db.conditions.update_one(
            {"id": condition["id"]},
            {"$set": condition},
            upsert=True
        )
