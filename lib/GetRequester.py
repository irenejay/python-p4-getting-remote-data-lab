import requests
import json
class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
       
        return response.content
    def load_json(self):
        response_body = self.get_response_body()
        try:
            json_data = json.loads(response_body)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None
        return json_data
  
    
    
    
    