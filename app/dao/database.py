from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017/")
db = client.medical_data


def get_db():
    return db


def initialize_database():
    # Initialize collections or indexes if needed
    db.encounters.create_index("participant.individual.reference")
    db.conditions.create_index("code.text")
    db.patients.create_index("id")
