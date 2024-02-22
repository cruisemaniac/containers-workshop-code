import random
from flask import Flask, jsonify, Response
import os

list_of_spots = [
    "Dubai Safari Park",
    "Dubai Frame",
    "Dubai Ferris wheel",
    "IMG Worlds of Adventure",
    "Dubai Parks and Resorts",
    "Mall of the Emirates",
    "Burj Khalifa",
    "Dubai Opera House",
    "City Walk",
    "Palm Jumeirah"
]

app = Flask(__name__)

# ‘/’ URL is bound with hello_world() function.
@app.route('/get_random_place')
def get_place():
    return jsonify({"GoTo": random.choice(list_of_spots)})

@app.route('/health')
def health_check():
    return Response(status=200)

# entrypoint
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=os.getenv("APP_PORT", 3000))
