from fastapi import APIRouter

router = APIRouter()

SLOTS = [
    {
        "slot_id": "SLOT1",
        "department": "cardiology",
        "datetime": "2025-01-22T10:00"
    }
]

@router.post("/slots")
def find_available_slots(department: str, date_range: str):
    return SLOTS

@router.post("/book")
def book_appointment(slot_id: str, patient_id: str):
    return {
        "appointment_id": "APT456",
        "patient_id": patient_id,
        "department": "cardiology",
        "provider": "Dr. Mehta",
        "datetime": "2025-01-22T10:00",
        "location": "City Hospital - Block A",
        "insurance_verified": True,
        "status": "confirmed"
    }
