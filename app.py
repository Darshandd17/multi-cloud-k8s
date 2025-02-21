import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Multi-Cloud Kubernetes Deployment!"

@app.errorhandler(404)
def page_not_found(e):
    return "Oops! Page not found.", 404

@app.route('/portal/redlion')
def redlion():
    return "Welcome to Redlion Portal!"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if not set
    app.run(host='0.0.0.0', port=port, threaded=True)
