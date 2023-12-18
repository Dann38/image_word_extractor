import os.path

import requests
HOST = "0.0.0.0"
PORT = 1281

url = f"http://localhost:{PORT}/word_extract/"

with open(os.path.join("img", "exm.txt")) as f:
    base_64 = f.read()

    rez = requests.post(url=url, json={
        "base64": base_64,
        "word_list": [{}],
        "text_list": ["string"]
        })
    print(rez.json()["word_list"])
    print(rez.json()["text_list"])
