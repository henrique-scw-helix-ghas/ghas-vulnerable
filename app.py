"""Intentionally vulnerable Flask app for the Helix GHAS sandbox. Do not deploy."""
import os
import sqlite3
import subprocess

from flask import Flask, request, send_file

app = Flask(__name__)
DB_PATH = "users.db"
FILES_DIR = "/srv/files"


@app.route("/users")
def find_user():
    name = request.args.get("name", "")
    cursor = sqlite3.connect(DB_PATH).cursor()
    # CWE-89: SQL built by string concatenation.
    cursor.execute("SELECT id, name FROM users WHERE name = '" + name + "'")
    return {"users": cursor.fetchall()}


@app.route("/files")
def read_file():
    filename = request.args.get("filename", "")
    # CWE-22: file path built from request input.
    return send_file(os.path.join(FILES_DIR, filename))


@app.route("/ping")
def ping():
    host = request.args.get("host", "127.0.0.1")
    # CWE-78: shell command built from request input.
    return subprocess.check_output("ping -c 1 " + host, shell=True)


@app.route("/hello")
def hello():
    name = request.args.get("name", "world")
    # CWE-79: request input reflected into HTML.
    return "<h1>Hello " + name + "</h1>"


if __name__ == "__main__":
    # CWE-489: debug mode exposes the Werkzeug debugger.
    app.run(debug=True)
