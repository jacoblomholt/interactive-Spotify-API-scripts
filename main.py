from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

Client_id = os.getenv("CLIENT_ID")
Client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_str = Client_id + ":" + Client_secret
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"

    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    # Website says it needs this form
    data = {"grant_type": "client_credentials"}

    # send a post request. Result is an object that includes some json data we need
    result = post(url, headers=headers, data=data)

    # read the json and make it a python object. In this scenario I think its a dictionary
    json_result = json.loads(result.content)

    # extract the value from key "access_token"
    token = json_result["access_token"]
    
    return token

def get_header(token):
    return {"Authorization": "Bearer " + token}
