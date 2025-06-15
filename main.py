from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files.get('file')
    if file:
        os.makedirs("loot", exist_ok=True)
        file.save(os.path.join("loot", file.filename))
        return "Received", 200
    return "Failed", 400

@app.route('/')
def home():
    return "OK", 200
