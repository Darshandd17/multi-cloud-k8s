import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Multi-Cloud Kubernetes Deployment!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if not set
    app.run(host='0.0.0.0', port=port, debug=False)
