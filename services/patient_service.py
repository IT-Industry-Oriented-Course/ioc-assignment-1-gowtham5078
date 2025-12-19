import requests

BASE_URL = "http://127.0.0.1:8000"

def search_patient(name: str):
    response = requests.post(
        f"{BASE_URL}/patients/search",
        params={"name": name}
    )
    return response.json()
