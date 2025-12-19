import requests

BASE_URL = "http://127.0.0.1:8000"

def find_slots(department: str, date_range: str):
    response = requests.post(
        f"{BASE_URL}/scheduling/slots",
        params={
            "department": department,
            "date_range": date_range
        }
    )
    return response.json()

def book_slot(slot_id: str, patient_id: str):
    response = requests.post(
        f"{BASE_URL}/scheduling/book",
        params={
            "slot_id": slot_id,
            "patient_id": patient_id
        }
    )
    return response.json()
