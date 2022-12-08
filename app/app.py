#!/usr/bin/env python3

import os
from flask import Flask, redirect
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

app = Flask(__name__)

try:
    ISSUER_URL = os.environ["ISSUER_URL"]
    AUTH_URL = os.environ["AUTH_URL"]
    TOKEN_URL = os.environ["TOKEN_URL"]
    USERINFO_URL = os.environ["USERINFO_URL"]
    JWKS_URL = os.environ["JWKS_URL"]
except Exception as ex:
    raise

@app.route('/')
def index():
    return 'Hello world!'

@app.route("/loogin")
def login():
    return redirect(AUTH_URL, code=302)

@app.route("/auth/callback")
def custom_callback():
    return "Logged in!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
