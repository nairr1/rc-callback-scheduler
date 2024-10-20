import requests

def queue_callback(api_base_url, access_token, skill_id, mobile_number):
  endpoint = "/incontactapi/services/v31.0/queuecallback"
  url = f"{api_base_url}{endpoint}?phoneNumber=%2B{mobile_number}&callerId=%2B{mobile_number}&skill={skill_id}&sequence=CB"

  response = requests.post(url, headers={
    'Accept-Encoding': 'zlib',
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {access_token}'
  })

  if response.status_code != 202:
    raise Exception(f"Error scheduling callback: {response.text}")

  return response.json()