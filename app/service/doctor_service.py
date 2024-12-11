from app.dao.database import get_db


def get_all_doctors():
    """
    Retrieve all unique doctors from the encounter data.
    Extract names and IDs from the `participant.individual.display` and `participant.individual.reference` fields
    where the display starts with "Dr.".
    """
    db = get_db()
    # Query encounters collection for relevant fields
    encounters = db.encounters.find({}, {"participant.individual": 1})
    doctors = {}

    for encounter in encounters:
        participant = encounter.get("participant", [])
        for part in participant:
            individual = part.get("individual", {})
            display = individual.get("display", "")
            reference = individual.get("reference", "")

            # Check if the display starts with "Dr."
            if display.startswith("Dr."):
                doctor_id = reference.split("|")[-1] if "|" in reference else reference  # Extract ID from reference
                doctors[doctor_id] = display

    # Convert dictionary to list of doctor objects
    return [{"id": doctor_id, "name": doctor_name} for doctor_id, doctor_name in
            sorted(doctors.items(), key=lambda x: x[1])]

