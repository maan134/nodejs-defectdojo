import requests

Url = 0
Token = 0
Test_id = 0
Tool_Result_file = 0
API_Endpoint = 0

headers = {
    'accept': 'application/json',
    'Authorization': 'Token 6aa3f54c2bd91951c7945dac26a8065a2314580c',
    # requests won't add a boundary if this header is set when you pass files=
    # 'Content-Type': 'multipart/form-data',
}

files = {
    'test': (None, '5'),
    '[email protected];type': (None, 'application/json'),
    'file': open('bandit_result.json', 'rb'),
    'scan_type': (None, 'Bandit Scan'),
    'tags': (None, 'test'),
}

response = requests.post('http://170.187.141.105:8080/api/v2/reimport-scan/', headers=headers, files=files)
