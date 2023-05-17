#!/usr/bin/env python3
"""
Web server Flask.
"""

from flask import Flask, jsonify, make_response
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.errorhandler(404)
def not_found(error):
    """Return a JSON-formatted 404 error response."""
    return make_response(jsonify({"error": "Not found"}), 404)

def main():
    """Run the web server."""
    app.run(host="0.0.0.0", port=5000)

if __name__ == "__main__":
    main()
