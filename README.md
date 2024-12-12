Microservices Project: AccessVerifier and ClientDataManager
This project consists of two microservices: AccessVerifier and ClientDataManager. These services are designed to manage and verify client access based on IP addresses from the AWS eu-west-1 region.
Overview
AccessVerifier: Verifies incoming requests based on allowed IP ranges.
ClientDataManager: Forwards requests to AccessVerifier and processes responses.
Prerequisites
Python 3.7+
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
Verifies if incoming requests are from allowed IPs.
Refreshes IP ranges every 24 hours.
ClientDataManager
1. Install Dependencies:
   pip install flask requests
2. Run the Service:
   python ClientDataManager.py
Functionality:
Forwards HTTP headers to AccessVerifier.
Processes requests based on AccessVerifier responses.
Testing
Use curl or Postman to send requests to ClientDataManager and verify access through AccessVerifier.
Example curl command:
