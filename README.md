# Medical Data Backend Application

This is a backend application built with **Flask** that periodically fetches medical data from provided endpoints, stores it in a database, and provides critical insights to doctors. The goal is to identify patients who may need additional care based on their medical history and conditions.

## Features

- **Periodic Data Fetching**: Periodically fetches patient, encounter, and condition data from external APIs.
- **Database**: Stores data in an **SQLite** database (or MongoDB for production).
- **API Endpoints**:
  - Get all patients.
  - Get all doctors.
  - Get all conditions.
  - Retrieve patients by doctor and condition.
- **Swagger Documentation**: Provides interactive API documentation using Swagger UI.

## Prerequisites

- **Python 3.x**
- **MongoDB** (optional for production)
- **Docker** (for containerization)
- **Python Virtual Environment** (recommended)


## API Endpoints

### 1. Get all conditions
**Endpoint**: `GET api/conditions`

**Response**: A list of all medical conditions in the system.

---

### 2. Get all doctors
**Endpoint**: `GET api/doctors`

**Response**: A list of all doctors in the system.

---

### 3. Get patients by doctor and condition
**Endpoint**: `POST api/patients/chronic-diseases

**Request Body**:

```json
{
  "doctor_id": 123456,
  "condition_codes": [101, 202]
}



