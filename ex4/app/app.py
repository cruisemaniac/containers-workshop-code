from flask import Flask, Response
import os
import requests

app = Flask(__name__)

# ‘/’ URL is bound with hello_world() function.
@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/wheredoigo')
def get_trip():
    resp = requests.get("http://"+os.getenv("API_SERVICE_URL", "api")+":4000/get_random_place")
    return resp.json()

@app.route('/health')
def health_check():
    return Response(status=200)
# entrypoint
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=os.getenv("APP_PORT", 3000))
