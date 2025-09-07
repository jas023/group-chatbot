from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # load your UI

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_msg = data.get("message", "")

    # Simple rule-based bot
    if "hello" in user_msg.lower():
        reply = "Hey there! 👋"
    elif "bye" in user_msg.lower():
        reply = "Goodbye, talk soon!"
    else:
        reply = f"You said: {user_msg}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
