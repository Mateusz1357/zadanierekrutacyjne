import requests
from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
import ipaddress

app = Flask(__name__)

allowed_ips = set()

def refresh_allowed_ips():
    global allowed_ips
    try:
        response = requests.get("https://ip-ranges.amazonaws.com/ip-ranges.json")
        response.raise_for_status()
        data = response.json()

        target_regions = {'eu-west-1'}

        new_allowed_ips = {
            ipaddress.ip_network(prefix['ip_prefix'])
            for prefix in data['prefixes']
            if prefix['region'] in target_regions
        }
        
        allowed_ips = new_allowed_ips
        print(f"Allowed IPs refreshed: {allowed_ips}")
    except requests.RequestException as e:
        print(f"Error fetching AWS IP ranges: {e}")
    except ValueError as e:
        print(f"Error processing IP ranges: {e}")

@app.route('/verify', methods=['POST'])
def verify():

    x_forwarded_for = request.headers.get('X-Forwarded-For')
    client_ip = x_forwarded_for.split(',')[0].strip() if x_forwarded_for else request.remote_addr
    print(f"Received request from IP: {client_ip}")

    try:
        client_ip_obj = ipaddress.ip_address(client_ip)

        if any(client_ip_obj in ip_range for ip_range in allowed_ips):
            return jsonify({"message": "Access granted"}), 200
    except ValueError:
        print(f"Invalid IP address format: {client_ip}")

    return jsonify({"message": "Access denied"}), 401

if __name__ == '__main__':

    scheduler = BackgroundScheduler()
    scheduler.add_job(refresh_allowed_ips, 'interval', hours=24)
    scheduler.start()


    refresh_allowed_ips()

    app.run(host='0.0.0.0', port=5001)
