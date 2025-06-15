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
    return "Listening..."

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render uses this
    app.run(host="0.0.0.0", port=port)
