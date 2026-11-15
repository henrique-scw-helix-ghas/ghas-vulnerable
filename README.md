# ghas-vulnerable

Intentionally vulnerable test code for the Helix GHAS sandbox. Do not deploy or reuse it.

CodeQL default setup and Dependabot alerts are on. Expected findings:

- `app.py` on `main`: SQL injection (CWE-89), path traversal (CWE-22), command injection (CWE-78), reflected XSS (CWE-79) and Flask debug mode (CWE-489).
- `admin.py` on the protected `release` branch only: unsafe deserialization (CWE-502).
- `report.py` in the open pull request only: code injection (CWE-94). Helix must not import pull request refs.
- `requirements.txt` and `package.json`: outdated packages with published advisories, reported by Dependabot.
