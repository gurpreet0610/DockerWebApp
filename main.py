from flask import Flask, request
import json
from controller.Utils import *
from flaskthreads import AppContextThread
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/payload", methods=['POST'])
def payload():
    # signature = request.headers.get('X-Hub-Signature')
    # data = request.data
    # if request.headers.get('X-GitHub-Event') == "push":
    #     print("push")
    data = request.data
    if(json.loads(data)["push"] == "True"):
        print("hey Lets PULL")
        t = AppContextThread(target=get_pull)
        t.start()
    return json.dumps({"success":True})

if __name__ == "__main__":
    app.run(debug=True,port=3000)
