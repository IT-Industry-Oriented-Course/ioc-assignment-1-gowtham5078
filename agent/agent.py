import json
from datetime import datetime
from huggingface_hub import InferenceClient

from agent.prompt import SYSTEM_PROMPT
from agent.validator import ValidationException

from services.patient_service import search_patient
from services.insurance_service import check_insurance
from services.scheduling_service import find_slots, book_slot
from config.settings import HF_API_KEY


MODEL_NAME = "meta-llama/Meta-Llama-3-8B-Instruct"


class ClinicalWorkflowAgent:
    def __init__(self, hf_api_key: str, dry_run: bool = False):
        self.client = InferenceClient(
            model=MODEL_NAME,
            token=hf_api_key
        )
        self.dry_run = dry_run

    def log_action(self, action: str, payload: dict, result: dict):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "action": action,
            "payload": payload,
            "result": result
        }
        with open("logs/audit_log.jsonl", "a") as f:
            f.write(json.dumps(log_entry) + "\n")

    def run(self, user_input: str):
        response = self.client.chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": (
                        SYSTEM_PROMPT
                        + "\n\nRespond ONLY with valid JSON.\n"
                        + "Format:\n"
                        + "{\n"
                        + '  "tool": "<tool_name>",\n'
                        + '  "arguments": { ... }\n'
                        + "}"
                    )
                },
                {"role": "user", "content": user_input}
            ],
            max_tokens=512,
            temperature=0.2
        )

        raw_content = response.choices[0].message.content

        try:
            model_output = json.loads(raw_content)
        except json.JSONDecodeError:
            raise ValidationException(
                f"Model did not return valid JSON:\n{raw_content}"
            )

        tool_name = model_output.get("tool")
        arguments = model_output.get("arguments")

        if not tool_name or not arguments:
            raise ValidationException("Invalid tool schema returned")

        if self.dry_run:
            return {
                tool_name: {
                    "status": "validated",
                    "arguments": arguments
                }
            }

        if tool_name == "search_patient":
            result = search_patient(**arguments)

        elif tool_name == "check_insurance_eligibility":
            result = check_insurance(**arguments)

        elif tool_name == "find_available_slots":
            result = find_slots(**arguments)

        elif tool_name == "book_appointment":
            result = book_slot(**arguments)

        else:
            raise ValidationException(f"Unknown tool: {tool_name}")

        self.log_action(tool_name, arguments, result)

        return {tool_name: result}
