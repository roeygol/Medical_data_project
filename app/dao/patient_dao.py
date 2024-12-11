from app.dao.database import get_db

db = get_db()


def save_patients(patients):
    db.patients.insert_many(patients)


def save_patients_upsert(patients):
    """
    Save patients to the database, ensuring no duplicates are inserted.
    """
    for patient in patients:
        db.patients.update_one(
            {"id": patient["id"]},
            {"$set": patient},
            upsert=True
        )


def find_patients_by_doctor_and_conditions(doctor_id, conditions):
    return list(
        db.patients.find(
            {"doctor_id": doctor_id, "conditions": {"$in": conditions}},
            {"_id": 0}
        )
    )
