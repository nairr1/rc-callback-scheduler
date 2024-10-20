import requests
import json

def fetch_access_token(base_url, access_key_id, access_key_secret, refresh_token=""):
  endpoint = "/authentication/v1/token/access-key"
  url = f"{base_url}{endpoint}"

  payload = {
    'accessKeyId': access_key_id,
    'accessKeySecret': access_key_secret
  }

  if refresh_token:
    payload['grant_type'] = 'refresh_token'
    payload['refresh_token'] = refresh_token

  response = requests.post(url, headers={
    'Accept': 'application/json',
    'Content-Type': 'application/json'
  }, data=json.dumps(payload))

  if response.status_code != 200:
    raise Exception(f"Error fetching access token: {response.text}")

  access_token_data = response.json()
  return access_token_data.get('access_token'), access_token_data.get('refresh_token', refresh_token)
