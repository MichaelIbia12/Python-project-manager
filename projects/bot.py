import requests
import json
from flask import Flask

app = Flask(__name__)

url = "https://graph.facebook.com/v17.0/127614807105987/messages"


@app.route("/webhook", methods=["POST"])
def handle_incoming_message():
    data = requests.get_json()
    if "messages" in data:
        for message in data["messages"]:
            text = message["message"]["content"]
            sender_id = message["from"]["id"]
            # Process the message and sender_id as needed
            # You can send a response here or store the message for later processing
    return jsonify({"success": True})

 
headers = {
    "Authorization": "Bearer EAAL58gP9zaIBOw3fQyaMhYrfxaxnizjYusppUqvDLKR1UMRmAufBmCpy2KhkcBCYpL1uZB7srTWASS4dPWLi3MNt6E90fyGVNnZADZC9fRfySZBk3sIi1ZBT5kzIayPHGcdU901dAaqvUWcYEViBS0QBZAyApNyGqooJUKN1A8xIZCnGsr5Sqg8dOZB9fDZCZBxQ4YUVnZCkpEmeQRS8vPZCvwsZD",
    "Content-Type": "application/json"
}

payload = {
    "messaging_product": "whatsapp",
    "to": "2349155332634",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
}
def handle_outgoing_message():
    response = requests.post(url, headers=headers, data=json.dumps(payload))


app.run(port=8080)