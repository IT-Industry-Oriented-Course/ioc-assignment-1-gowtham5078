
from pydantic import BaseModel, Field


class AppointmentConfirmation(BaseModel):
    appointment_id: str = Field(
        ...,
        description="Unique appointment identifier"
    )
    patient_id: str = Field(
        ...,
        description="Unique patient identifier"
    )
    department: str = Field(
        ...,
        description="Clinical department"
    )
    provider: str = Field(
        ...,
        description="Assigned healthcare provider"
    )
    datetime: str = Field(
        ...,
        description="Scheduled appointment datetime in ISO format"
    )
    location: str = Field(
        ...,
        description="Clinic or hospital location"
    )
    insurance_verified: bool = Field(
        ...,
        description="Whether insurance eligibility was verified"
    )
    status: str = Field(
        ...,
        description="Appointment status (confirmed/cancelled)"
    )

    class Config:
        json_schema_extra = {
            "example": {
                "appointment_id": "APT456",
                "patient_id": "PAT123",
                "department": "Cardiology",
                "provider": "Dr. Mehta",
                "datetime": "2025-01-22T10:00",
                "location": "City Hospital - Block A",
                "insurance_verified": True,
                "status": "confirmed"
            }
        }
