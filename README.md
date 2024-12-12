AccessVerifier and ClientDataManager
This project comprises two microservices—AccessVerifier and ClientDataManager—designed to manage and verify client access based on IP addresses from the AWS eu-west-1 region.

Overview
AccessVerifier: Validates incoming requests against allowed IP ranges.
ClientDataManager: Forwards requests to AccessVerifier and processes the responses.
Prerequisites
Python 3.7 or higher
Docker (optional, for containerization)
Kubernetes (optional, for deployment)

Setup
AccessVerifier

Install Dependencies:
pip install flask requests apscheduler

Run the Service:

python AccessVerifier.py

Functionality:

Fetches AWS IP ranges for the eu-west-1 region.
Verifies if incoming requests originate from allowed IPs.
Refreshes IP ranges every 24 hours.


ClientDataManager

Install Dependencies:

pip install flask requests

Run the Service:


python ClientDataManager.py

Functionality:

Forwards HTTP headers to AccessVerifier.
Processes requests based on AccessVerifier's responses.
Testing
Use curl or Postman to send requests to ClientDataManager and verify access through AccessVerifier.

Example curl command:

curl -X GET http://localhost:5000/your-endpoint -H "Your-Header: header-value"
