import requests
import json

class AnkiAPI:
    def __init__(self, url="http://localhost:8765"):
        self.url = url 
    def _request(self, action, params={}):
        payload = {
            "action": action,
            "version": 6,
            "params": params
        }
        response = requests.post(self.url, json=payload).json()
        
        if len(response) != 2:
            raise Exception("Response has an unexpected number of fields")
        if 'error' not in response:
            raise Exception("Response is missing required error field")
        if 'result' not in response:
            raise Exception("Response is missing required result field")
        if response['error'] is not None:
            raise Exception(f"AnkiConnect Error: {response['error']}")
        return response['result']
    def add_note(self, deck_name, model_name, front, back):
        note = {
            "deckName": deck_name,
            "modelName": model_name,
            "fields": {
                "Front": front,
                "Back": back
            },
            "options": {
                "allowDuplicate": False
            },
            "tags": ["auto-generated"]
        }
        return self._request("addNote", {"note": note})
    
if __name__ == "__main__":
    anki = AnkiAPI()
    try:
        anki.add_note("Default", "Basic", "puisto", "park")
        print("Card added successfully!")
    except Exception as e:
        print(f"Failed to add card: {e}")

