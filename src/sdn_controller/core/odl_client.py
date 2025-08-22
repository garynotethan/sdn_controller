import requests
from requests.auth import HTTPBasicAuth

class ODLClient:

    def __init__(self, host='127.0.0.1', port='8181', username='admin', password='admin'):
        self.base_url = f'http://{host}:{port}/restconf'
        self.auth = HTTPBasicAuth(username, password)
        self.headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
