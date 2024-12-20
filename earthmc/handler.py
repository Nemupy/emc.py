import requests

base_url = "https://api.earthmc.net/v3/aurora/"

def get(endpoint="", query_name=None):
    url = base_url + endpoint
    
    try:
        if query_name:
            data = {"query": [query_name]}
            response = requests.post(url, json=data)
        else:
            response = requests.get(url)
        
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as error:
        print(error)
        return None