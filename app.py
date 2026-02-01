from flask import Flask, request
import sqlite3

app = Flask(__name__)

# Added after pipeline setup to validate Gitleaks
GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef"

def get_db():
    return sqlite3.connect("users.db")

@app.route("/")
def home():
    return "SecureRelease Demo App"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
