from app.dao.database import get_db


def find_patients_with_conditions(doctor_id, conditions):
    """
    Find all patients who:
    - Have seen the specified doctor at least once
    - Have been diagnosed with one or more of the specified conditions
    """
    db = get_db()

    # Step 1: Find patients who have seen the specified doctor
    encounters = db.encounters.find(
        {"participant.individual.reference": {"$regex": f"Practitioner.*{doctor_id}"}},
        {"subject.reference": 1}
    )
    patients_by_doctor = {encounter["subject"]["reference"] for encounter in encounters}

    # Step 2: Find patients diagnosed with specified conditions
    conditions_query = {"code.text": {"$in": conditions}}
    conditions_data = db.conditions.find(conditions_query, {"subject.reference": 1})
    patients_by_conditions = {condition["subject"]["reference"] for condition in conditions_data}

    # Step 3: Intersection of both sets
    matched_patients = patients_by_doctor.intersection(patients_by_conditions)

    # Step 4: Retrieve patient details
    patients = db.patients.find({"id": {"$in": list(matched_patients)}}, {"name": 1, "id": 1})
    return [{"id": patient["id"], "name": patient.get("name", "Unknown")} for patient in patients]
