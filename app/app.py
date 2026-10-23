import os
from flask import Flask, jsonify

app = Flask(__name__)

VERSION = os.getenv("APP_VERSION", "1.0.0")
FORCE_FAILURE = os.getenv("FORCE_FAILURE", "false").lower() == "true"


@app.route("/")
def home():
    return jsonify({
        "project": "CI/CD Pipeline with Automated Rollback",
        "version": VERSION,
        "status": "running"
    })


@app.route("/health")
def health():
    if FORCE_FAILURE:
        return jsonify({"status": "unhealthy"}), 500

    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)