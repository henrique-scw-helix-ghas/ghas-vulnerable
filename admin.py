"""Release-branch-only endpoint for the Helix GHAS sandbox. Do not deploy."""
import pickle

from flask import request

from app import app


@app.route("/admin/import", methods=["POST"])
def import_settings():
    # CWE-502: deserializes untrusted request data.
    settings = pickle.loads(request.get_data())
    return {"keys": sorted(settings)}
