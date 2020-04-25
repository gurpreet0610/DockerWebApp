from flask import Flask,  jsonify
from flask import render_template # for render_template
from flask import request # for getting user input from HTML page
import requests
import json
import os

"""python2 pagekite.py  3000 gurpreetsingh.pagekite.me"""
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
        x=os.system("git pull")
        print(x)
        y=os.system("cd /home/gurpreet/Code/github/DockerWebApp/ && docker-compose up -d ")
        print("Error Code ->"+str(y))
        if(y!=0):
            print("Error Occured During Build")
            z=os.system("cd /home/gurpreet/Code/github/DockerWebApp/ && git reset --hard HEAD@{1} ")
            y=os.system("cd /home/gurpreet/Code/github/DockerWebApp/ && docker-compose up -d ")
            print("Error Code ->"+str(y))
            
            
       
    return json.dumps({"success":True})

if __name__ == "__main__":
    app.run(debug=True,port=3000)
