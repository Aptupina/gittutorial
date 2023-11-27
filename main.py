from flask import Flask, request
import logging
import json

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

@app.route("/",methods=["POST"])
def main():
    logging.info(request.join)

    response = {
        "version":request.json["version"],
        "session":request.json["session"],
        "response": {
            "end_session": False
        }
    }

    req = request.join
    if req["session"]["new"]:
        response["response"]["text"] = "Привет! Я капибара"
    return json.dumps(response)