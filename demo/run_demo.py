from agent.agent import ClinicalWorkflowAgent
from config.settings import HF_API_KEY

agent = ClinicalWorkflowAgent(hf_api_key=HF_API_KEY)

request = "Schedule a cardiology follow-up for patient Ravi Kumar next week and check insurance eligibility"

result = agent.run(request)

print(result)

refusal = agent.run("Should I prescribe beta blockers to Ravi Kumar?")

print(refusal)
