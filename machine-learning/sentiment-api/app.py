from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route("/")
def hello_api():
    return 'Hello, from a simple sentiment-api!'

@app.route("/predict", methods=["POST"])
def sentiment():
    data = request.get_json()
    text = data.get("text", "")
    # Dummy sentiment logic
    sentiment_result = "positive" if "love" in text.lower() else "neutral"
    confidence = 0.95
    return jsonify({"sentiment": sentiment_result, "confidence": confidence})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)