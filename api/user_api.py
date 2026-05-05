import requests
from config import CREATE_USER_ENDPOINT, USER_DATA_ENDPOINT

def create_user(payload):
    return requests.post(CREATE_USER_ENDPOINT, json=payload)

def delete_user(token):
    headers = {
        "Authorization": token
    }   
    return requests.delete(USER_DATA_ENDPOINT, headers=headers)
