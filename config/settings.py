import os

HF_API_KEY = os.getenv("HF_API_KEY")
DRY_RUN = os.getenv("DRY_RUN", "false").lower() == "true"
