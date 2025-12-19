
from pydantic import BaseModel, Field


class InsuranceStatus(BaseModel):
    patient_id: str = Field(
        ...,
        description="Unique patient identifier"
    )
    eligible: bool = Field(
        ...,
        description="Whether insurance coverage is active"
    )
    payer: str = Field(
        ...,
        description="Insurance provider name"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "patient_id": "PAT123",
                "eligible": True,
                "payer": "ABC Health Insurance"
            }
        }
