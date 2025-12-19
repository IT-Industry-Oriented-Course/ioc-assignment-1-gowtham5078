

from pydantic import BaseModel, Field
from typing import Optional


class Patient(BaseModel):
    patient_id: str = Field(
        ...,
        description="Unique patient identifier"
    )
    full_name: str = Field(
        ...,
        description="Full legal name of the patient"
    )
    date_of_birth: str = Field(
        ...,
        description="Date of birth in YYYY-MM-DD format"
    )
    gender: Optional[str] = Field(
        None,
        description="Gender of the patient"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "patient_id": "PAT123",
                "full_name": "Ravi Kumar",
                "date_of_birth": "1987-04-12",
                "gender": "male"
            }
        }
