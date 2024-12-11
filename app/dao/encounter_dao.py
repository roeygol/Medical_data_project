from .database import get_db

db = get_db()


def save_encounters(encounters):
    db.encounters.insert_many(encounters)


def save_encounters_upsert(encounters):
    """
    Save encounters to the database, ensuring no duplicates are inserted.
    """
    for encounter in encounters:
        db.encounters.update_one(
            {"id": encounter["id"]},
            {"$set": encounter},
            upsert=True
        )
