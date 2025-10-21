from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_api():
    return 'Hello, from a simple sentiment-api!'

@app.route("/predict")
def sentiment():
    return 

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)