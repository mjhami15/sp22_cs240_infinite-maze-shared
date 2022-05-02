from flask import Flask, render_template, request, jsonify
import os
import requests
import json

app = Flask(__name__)

#Route for getting MG data
@app.route('/', methods=["GET"])
def mg():
    response = jsonify({"geom": ["988088c", "1202004", "5f7f104", "0edb000", "592c104", "57d7104", "3a28226"]})
    response.headers["Content-Type"] = "application/json"
    response.headers["Age"] = 0
    response.headers["Cache-Control: max-age"] = 3600
    return response, 200