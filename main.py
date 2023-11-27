from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST'])
def webhook():
    try:
        data = request.json
        text = data.get('request', {}).get('command')
        response_text = "Assalamu aleykum"

        response = {
            'response': {
                'text': response_text,
                'end_session': False
            },
            'version': '1.0'
        }

Send response to the provided webhook
        webhook_url = "https://hkdk.events/656RgpXWrrjC"
        requests.post(webhook_url, json=response)

        return jsonify(response)
    except Exception as e:
        return jsonify({'error': str(e)})

if name == 'main':
    app.run(debug=True)
