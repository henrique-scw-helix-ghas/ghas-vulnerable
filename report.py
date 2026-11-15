"""Pull-request-only endpoint for the Helix GHAS sandbox. Do not deploy."""
from flask import request

from app import app


@app.route("/report")
def report():
    expression = request.args.get("expr", "0")
    # CWE-94: evaluates request input as Python code.
    return {"result": eval(expression)}
