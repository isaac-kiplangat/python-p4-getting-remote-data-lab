import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url
        self.response = requests.get(url)

    def get_response_body(self):
        return self.response.content

    def load_json(self):
        try:
            json_content = self.response.json()
            return json_content
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return None  

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')
get_requester.load_json()
