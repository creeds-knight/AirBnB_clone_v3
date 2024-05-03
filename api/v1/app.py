#!/usr/bin/python3
"""app"""
from api.v1.views import app_views
from flask import Flask
from flask import jsonify
from models import storage
import os


app = Flask(__name__)
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def teardown(exc):
    """ closes the session """
    storage.close()

@app.errorhandler(404)
def page_not_found(e):
    """ Handling the page not found """
    return jsonify({"error":"Not found"})



if __name__ == "__main__":
    host = os.getenv("HBNB_API_HOST", "0.0.0.0")
    port = int(os.getenv("HBNB_API_PORT", 5000))
    app.run(debug=True, host=host, port=port, threaded=True)
