
TOOLS = [
    {
        "name": "search_patient",
        "description": "Search for a patient using full name",
        "parameters": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string",
                    "description": "Full name of the patient"
                }
            },
            "required": ["name"]
        }
    },
    {
        "name": "check_insurance_eligibility",
        "description": "Check insurance eligibility for a patient",
        "parameters": {
            "type": "object",
            "properties": {
                "patient_id": {
                    "type": "string",
                    "description": "Unique patient identifier"
                }
            },
            "required": ["patient_id"]
        }
    },
    {
        "name": "find_available_slots",
        "description": "Find available appointment slots for a department",
        "parameters": {
            "type": "object",
            "properties": {
                "department": {
                    "type": "string"
                },
                "date_range": {
                    "type": "string",
                    "description": "Example: next week"
                }
            },
            "required": ["department", "date_range"]
        }
    },
    {
        "name": "book_appointment",
        "description": "Book an appointment slot for a patient",
        "parameters": {
            "type": "object",
            "properties": {
                "slot_id": {
                    "type": "string"
                },
                "patient_id": {
                    "type": "string"
                }
            },
            "required": ["slot_id", "patient_id"]
        }
    }
]
