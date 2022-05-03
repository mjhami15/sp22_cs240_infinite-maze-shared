from flask import Flask, render_template, request, jsonify
import os
import requests
import json
import random

app = Flask(__name__)

@app.route("/")
def add_to_list():
    r = requests.put("http://127.0.0.1:5000/addMG", json={"name": "stndrd MG1", "url": "http://127.0.0.1:24002/", "author": "Matt Hamilton", "weight": 1})
    return jsonify({"Added": "MG"}), 200

#Route for getting MG data
@app.route('/generate', methods=["GET"])
def mg():
    one = {"geom": ["b8a0a8e", "d7b0e7d", "1ae5ba4", "4dd5dd1", "1430614", "53e5b65", "3aa0aa6"]}
    two = {"geom": ["9aa0aac", "5984ba4", "5320ae5", "0a808a0", "1e575d5", "5b0c575", "3a202a6"]}
    three = {"geom": ["9c92c9c", "1269224", "1cb0e96", "02e5b0a", "1cb0c3c", "53c3284", "3e38a67"]}
    four = {"geom": ["9eb0edd", "3880a06", "9677d7d", "2cdd5b0", "9630086", "3cd757d", "b2282a6"]}
    choices = [one, two, three, four]
    choice = random.choice(choices)
    response = jsonify(choice)
    response.headers["Content-Type"] = "application/json"
    response.headers["Cache-Control"] = 'no-store'
    return response, 200