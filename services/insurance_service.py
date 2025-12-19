import requests

BASE_URL = "http://127.0.0.1:8000"

def check_insurance(patient_id: str):
    response = requests.post(
        f"{BASE_URL}/insurance/check",
        params={"patient_id": patient_id}
    )
    return response.json()
