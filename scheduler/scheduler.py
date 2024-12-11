import requests
import ndjson
from app.dao.patient_dao import save_patients_upsert
from app.dao.condition_dao import save_conditions_upsert
from app.dao.encounter_dao import save_encounters_upsert

PATIENT_NEW_URL = "https://pphp-static.diagnosticrobotics.com/sample/New_Patient.ndjson"
CONDITION_NEW_URL = "https://pphp-static.diagnosticrobotics.com/sample/New_Condition.ndjson"
ENCOUNTER_NEW_URL = "https://pphp-static.diagnosticrobotics.com/sample/New_Encounter.ndjson"


def schedule_fetch_and_store_data():
    """
    Fetch NEW data from the provided endpoints, parse it, and store it in the database.
    """
    try:
        # Fetch patients
        patient_response = requests.get(PATIENT_NEW_URL)
        patient_response.raise_for_status()
        patient_data = list(ndjson.loads(patient_response.text))
        save_patients_upsert(patient_data)
        print(f"Fetched and saved {len(patient_data)} New patients.")

        # Fetch conditions
        condition_response = requests.get(CONDITION_NEW_URL)
        condition_response.raise_for_status()
        condition_data = list(ndjson.loads(condition_response.text))
        save_conditions_upsert(condition_data)
        print(f"Fetched and saved {len(condition_data)} New conditions.")

        # Fetch encounters
        encounter_response = requests.get(ENCOUNTER_NEW_URL)
        encounter_response.raise_for_status()
        encounter_data = list(ndjson.loads(encounter_response.text))
        save_encounters_upsert(encounter_data)
        print(f"Fetched and saved {len(encounter_data)} New encounters.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")