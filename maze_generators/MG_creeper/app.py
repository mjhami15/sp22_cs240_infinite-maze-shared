from flask import Flask, render_template, request, jsonify
import os
import requests
import json

app = Flask(__name__)

#Route for getting MG data
@app.route("/")
def add_to_list():
    r = requests.put("http://sp22-cs240-adm.cs.illinois.edu:24000/addMG", json={"name": "Creeper (Static) [REAL]", "url": "http://172.22.152.32:24011", "author": "Matt Hamilton", "weight": 1})
    return jsonify({"Added": "MG"}), 200

@app.route('/generate', methods=["GET"])
def mg():
    response = jsonify({"geom": ["988088c", "1202004", "5f7f104", "0edb000", "592c104", "57d7104", "3a28226"]})
    response.headers["Content-Type"] = "application/json"
    response.headers["Age"] = 0
    response.headers["Cache-Control: max-age"] = 3600
    return response, 200