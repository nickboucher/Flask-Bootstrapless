#!/usr/bin/env python3
from flask import Flask, render_template
from assets import Assets

app = Flask(__name__)
# All static assets are compiled, minified, and included via assets.py
Assets(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()
