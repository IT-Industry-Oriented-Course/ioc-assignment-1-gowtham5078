from fastapi import APIRouter

router = APIRouter()

PATIENTS_DB = {
    "ravi kumar": {
        "patient_id": "PAT123",
        "full_name": "Ravi Kumar",
        "date_of_birth": "1987-04-12",
        "gender": "male"
    }
}

@router.post("/search")
def search_patient(name: str):
    return PATIENTS_DB.get(name.lower())
