from dotenv import load_dotenv
load_dotenv()

from agent.agent import ClinicalWorkflowAgent
from config.settings import HF_API_KEY, DRY_RUN


def main():
    if not HF_API_KEY:
        raise RuntimeError("HF_API_KEY is not set. Check your .env file.")

    agent = ClinicalWorkflowAgent(
        hf_api_key=HF_API_KEY,
        dry_run=DRY_RUN
    )

    print("Clinical Workflow Agent Ready")
    user_input = input("> ")

    result = agent.run(user_input)
    print(result)


if __name__ == "__main__":
    main()
