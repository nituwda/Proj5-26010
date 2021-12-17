import requests
access_token = 'MDQyMTE5NDItN2VjOS00YWIzLTlmY2YtOWNkNzUzNGZlYTg0ZDI2YjQ4MmQtMzhk_P0A1_23ca1dfa-ad8d-4383-9b62-45cb7418ddf7'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vYzQ0NmE0NjAtNWYwMi0xMWVjLWE1OGMtNDk3MTliMGI3NWRh'
url= 'https://webexapis.com/v1/rooms/{}/meetingInfo'.format(room_id)
headers = {
    'Authorization': 'Bearer {}'.format(access_token),'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(res.json())