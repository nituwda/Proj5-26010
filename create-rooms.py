import requests
access_token = 'MDQyMTE5NDItN2VjOS00YWIzLTlmY2YtOWNkNzUzNGZlYTg0ZDI2YjQ4MmQtMzhk_P0A1_23ca1dfa-ad8d-4383-9b62-45cb7418ddf7'
url= 'https://webexapis.com/v1/rooms'
headers = {
    'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json'
}
params={
    'title': 'DevNet Associate Training!'
}
res = requests.post(url, headers=headers, json=params)
print(res.json())