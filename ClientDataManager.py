import requests
from flask import Flask, request

app = Flask(__name__)

ACCESS_VERIFIER_URL = "http://localhost:5001/verify"

@app.route('/process', methods=['POST'])
def process_request():
    headers = {key: value for key, value in request.headers.items()}
    try:
        response = requests.post(ACCESS_VERIFIER_URL, headers=headers)

        if response.status_code == 200:
            return "Request processed successfully", 200
        else:
            return "Access denied", 401
    except requests.RequestException as e:
        print(f"Error connecting to AccessVerifier: {e}")
        return "Internal Server Error", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
