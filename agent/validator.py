

from pydantic import ValidationError
from schemas.patient import Patient
from schemas.insurance import InsuranceStatus
from schemas.appointment import AppointmentConfirmation


class ValidationException(Exception):
    """Raised when schema validation fails"""
    pass


def validate_patient(data: dict) -> Patient:
    try:
        return Patient(**data)
    except ValidationError as e:
        raise ValidationException(f"Invalid patient data: {e}")


def validate_insurance(data: dict) -> InsuranceStatus:
    try:
        return InsuranceStatus(**data)
    except ValidationError as e:
        raise ValidationException(f"Invalid insurance data: {e}")


def validate_appointment(data: dict) -> AppointmentConfirmation:
    try:
        return AppointmentConfirmation(**data)
    except ValidationError as e:
        raise ValidationException(f"Invalid appointment data: {e}")
