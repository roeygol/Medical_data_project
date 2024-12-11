import requests
import ndjson
from app.dao.patient_dao import save_patients
from app.dao.condition_dao import save_conditions
from app.dao.encounter_dao import save_encounters


PATIENT_URL = "https://pphp-static.diagnosticrobotics.com/sample/Patient.ndjson"
CONDITION_URL = "https://pphp-static.diagnosticrobotics.com/sample/Condition.ndjson"
ENCOUNTER_URL = "https://pphp-static.diagnosticrobotics.com/sample/Encounter.ndjson"


def fetch_and_store_data():
    """
    Fetch data from the provided endpoints, parse it, and store it in the database.
    """
    try:
        # Fetch patients
        patient_response = requests.get(PATIENT_URL)
        patient_response.raise_for_status()
        patient_data = list(ndjson.loads(patient_response.text))
        save_patients(patient_data)
        print(f"Fetched and saved {len(patient_data)} patients.")

        # Fetch conditions
        condition_response = requests.get(CONDITION_URL)
        condition_response.raise_for_status()
        condition_data = list(ndjson.loads(condition_response.text))
        save_conditions(condition_data)
        print(f"Fetched and saved {len(condition_data)} conditions.")

        # Fetch encounters
        encounter_response = requests.get(ENCOUNTER_URL)
        encounter_response.raise_for_status()
        encounter_data = list(ndjson.loads(encounter_response.text))
        save_encounters(encounter_data)
        print(f"Fetched and saved {len(encounter_data)} encounters.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except Exception as e:
        print(f"Error processing data: {e}")