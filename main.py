from flask import Flask, render_template, request, jsonify
import os
import time

app = Flask(__name__)

# Global variables to store user inputs
TARGET_NUMBER = None
MESSAGES = []
HATER_NAME = None
DELAY = None

# Home route
@app.route("/")
def index():
    return render_template("index.html")

# Send messages route
@app.route("/send", methods=["POST"])
def send():
    global TARGET_NUMBER, MESSAGES, HATER_NAME, DELAY
    try:
        # Get form data
        TARGET_NUMBER = request.form.get("target_number")
        message_file = request.files.get("message_file")
        HATER_NAME = request.form.get("hater_name")
        DELAY = int(request.form.get("delay"))

        # Read messages from file
        if message_file:
            MESSAGES = message_file.read().decode("utf-8").splitlines()
        else:
            return jsonify({"status": "error", "message": "No message file uploaded."})

        # Simulate sending messages (replace with actual WhatsApp API logic)
        for message in MESSAGES:
            full_message = f"{HATER_NAME} {message}"
            print(f"Sending to {TARGET_NUMBER}: {full_message}")  # Simulate sending
            time.sleep(DELAY)

        return jsonify({"status": "success", "message": "Messages sent successfully!"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
