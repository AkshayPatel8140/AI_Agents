from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

# @app.route("/")
# def index():
#     return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    messages = data.get("messages", [])

    response = requests.post(
        "http://localhost:11434/api/chat",
        json={"model": "phi3", "messages": messages, "stream": True},
        stream=True,  # Important!
    )

    full_reply = ""
    for line in response.iter_lines():
        if line:
            json_data = json.loads(line.decode("utf-8"))
            full_reply += json_data.get("message", {}).get("content", "")

    return jsonify({"reply": full_reply})


if __name__ == "__main__":
    app.run(debug=True)
