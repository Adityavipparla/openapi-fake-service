
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"users": ["Alice", "Bob"]})

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(port=5000)