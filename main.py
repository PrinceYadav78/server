from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file', 400
    f = request.files['file']
    os.makedirs('loot', exist_ok=True)
    f.save(os.path.join('loot', f.filename))
    return 'Uploaded', 200

@app.route('/')
def index():
    return "Listening...", 200

if __name__ == '__main__':
    app.run()
