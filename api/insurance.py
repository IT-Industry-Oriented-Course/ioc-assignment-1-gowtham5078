from fastapi import APIRouter

router = APIRouter()

@router.post("/check")
def check_insurance(patient_id: str):
    return {
        "patient_id": patient_id,
        "eligible": True,
        "payer": "ABC Health Insurance"
    }
