from flask import render_template
from app import app

from flask import request
from flask import jsonify
@app.route('/')
def index():
    return render_template('index.html')

@app.route("/subans", methods=["POST"])
def subans():
    jsdata = request.form["canvas_data"]
    print("helllllllllllloooooooooooooo")
    print(jsdata)
    return jsonify(jsdata)