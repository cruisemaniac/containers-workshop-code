from flask import Flask

app = Flask(__name__)

# ‘/’ URL is bound with hello_world() function.
@app.route('/')
def hello_world():
    return 'Hello World'

# entrypoint
if __name__ == '__main__': 
    app.run(debug=True, host='0.0.0.0', port=4000)
