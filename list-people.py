import requests
import json
access_token = 'MDQyMTE5NDItN2VjOS00YWIzLTlmY2YtOWNkNzUzNGZlYTg0ZDI2YjQ4MmQtMzhk_P0A1_23ca1dfa-ad8d-4383-9b62-45cb7418ddf7'
url = 'https://webexapis.com/v1/people'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json'
}
params = {
    'email': 'devdan.romulo.iics@ust.edu.ph'
}
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))
# Y2lzY29zcGFyazovL3VzL1BFT1BMRS84ODBiZWE1OS03YTllLTQ2YTAtYTQ2My1kMGYwMmVlYTQ0YmE - aldrin
# Y2lzY29zcGFyazovL3VzL1BFT1BMRS9iYWY1NDc0Ny0wODhjLTQwYjUtOTM1OC0xZjBmNDBhYjYyYmI - jc 
# Y2lzY29zcGFyazovL3VzL1BFT1BMRS9jN2FjMjY3Yy1iZmJiLTQyODQtOTZmNi1lMjMxNTE3NDE5N2I - dev