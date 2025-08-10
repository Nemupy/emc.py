import requests

BASE_URL = "https://api.earthmc.net/v3/aurora/"

def get(endpoint: str = "", queries = None, template: dict = None):
    url = BASE_URL + endpoint
    
    if queries:
        body = {"query": queries}
    if template:
        body["template"] = template

    try:
        response = requests.get(url, json=body)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"[POST ERROR] {url}: {e}")
        return None
