import json
import requests
from flask import Flask, jsonify, request


# Load OpenAPI spec
def load_openapi_spec(filepath):
    with open(filepath, 'r') as f:
        spec = json.load(f)
    return spec

# Extract endpoints from OpenAPI

def extract_endpoints(spec):
    endpoints = []
    for path, methods in spec.get("paths", {}).items():
        for method in methods:
            endpoints.append({"method": method.lower(), "path": path})
    return endpoints

# Start mock server (minimal example)

def start_mock_server():
    app = Flask(__name__)

    @app.route('/<path:any_path>', methods=["GET", "POST", "PUT", "DELETE"])
    def catch_all(any_path):
        return jsonify({"message": f"Mock response for {request.method} /{any_path}"}), 200

    app.run(debug=True, port=5000)

# Simple test runner for endpoints

def test_endpoints(base_url, endpoints):
    for endpoint in endpoints:
        url = base_url + endpoint["path"].replace('{', '').replace('}', '')  # Remove path params for now
        try:
            if endpoint["method"] == "get":
                resp = requests.get(url)
            elif endpoint["method"] == "post":
                resp = requests.post(url, json={})
            else:
                continue
            print(f"{endpoint['method'].upper()} {url} => {resp.status_code}")
        except Exception as e:
            print(f"Error calling {endpoint['method'].upper()} {url}: {e}")

# Main flow
if __name__ == "__main__":
    spec = load_openapi_spec("Code.json")
    endpoints = extract_endpoints(spec)

    print("\n[Parsed Endpoints]")
    for e in endpoints:
        print(e)

    print("\n[Testing Endpoints Against Mock Server]")
    test_endpoints("http://localhost:5000", endpoints)

    # Uncomment below line to run the mock server
    start_mock_server()



