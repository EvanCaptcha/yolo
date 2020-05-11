import requests
import threading
from flask import Flask, render_template, request
import random
import time
app = Flask(__name__)
threads = 1
p = True
headers = {
    'authority': 'onyolo.com',
    'accept': 'application/json, text/plain, */*',
    'origin': 'https://onyolo.com',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36',
    'content-type': 'application/json;charset=UTF-8',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'cors',
    'referer': 'https://onyolo.com/m/4uHac0RTNY',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
}


@app.route("/")
def home():
    return render_template("index.html")
def task(user, txt):
    sent = 0
    data = '{"text":"' + txt + '","cookie":""}'
    for x in range(50):
            try:
                s = requests.session()
                if p:
                    lines = open('/root/yolo/proxies').read().splitlines()
                    proxy = random.choice(lines)
                    split = proxy.split(":")
                    proxies = {"https": "https://" + split[0] + ":" + split[1]}
                    print(proxies)
                    s.proxies.update(proxies)
                response = s.post('https://onyolo.com/' + user + '/message', headers=headers, data=data)
                print(response.status_code)
                if response.text == 'ok':
                    print('Message sent to ' + user)
                    sent =+1
            except:
                pass
    else:
        pass
@app.route("/spam", methods=["POST", "GET"])
def spam():
    if request.method == "POST":
        link = request.form["uid"]
        msg = request.form["msg"]
        # create threads

        uid = link.split('/')[4].split('?')[0]
        time.sleep(10)
        jobs = []
        for i in range(0, threads):
            jobs.append(threading.Thread(target=task(user=uid, txt=msg)))

        # start  threads
        for j in jobs:
            j.start()

        # ensure all threads have been finished
        for j in jobs:
            j.join()
        return "Success"
    elif request.method == 'GET':
        return "Wrong method."
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')
