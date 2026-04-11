import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()
BASE_URL = os.getenv('BASE_URL')
print('BASE_URL', BASE_URL)
with open('test_data/profile.json') as f:
    data = json.load(f)
payload = data['login_valid_user']
resp = requests.post(f'{BASE_URL}/users/login', json=payload, verify=False)
print('LOGIN', resp.status_code, resp.text)
if resp.status_code != 200:
    raise SystemExit('login failed')

token = resp.json()['data']['jwtToken']
shopper_id = resp.json()['data']['userId']
headers = {'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'}
update_payload = data['update_user']
for method in ['put', 'patch', 'post']:
    func = getattr(requests, method)
    r = func(f'{BASE_URL}/shoppers/{shopper_id}', headers=headers, json=update_payload, verify=False)
    print(method.upper(), r.status_code, repr(r.text[:200]))
