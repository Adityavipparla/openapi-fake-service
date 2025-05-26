# OpenAPI Fake Service
This project loads an OpenAPI spec from `Code.json`, reads all endpoints, and tests them using a mock Flask server.
Reads an OpenAPI spec (Code.json)

Identifies all endpoints from the spec

Starts a mock API server (mock_server.py) that pretends to be the real service

Sends requests to all endpoints to verify they respond correctly

