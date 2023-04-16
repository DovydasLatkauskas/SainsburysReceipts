from dataclasses import dataclass


@dataclass
class ApiToken:
        client_id: str = ''
        client_secret: str = ''
        username: str = ''
        api_key: str = ''
        

