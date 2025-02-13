from flask import Flask, render_template, request, jsonify
import pywhatkit as kit
import time
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    # Get user inputs from the form
    target_number = request.form['target_number']
    message_file_path = request.form['message_file']
    message_delay = int(request.form['message_delay'])
    hater_name = request.form['hater_name']

    # Read messages from the file
    with open(message_file_path, 'r') as file:
        messages = file.read().splitlines()

    # Send messages in a loop
    for message in messages:
        full_message = f"{hater_name} {message}"
        try:
            kit.sendwhatmsg_instantly(target_number, full_message)
            print(f"Message sent to {target_number}: {full_message}")
            time.sleep(message_delay)
        except Exception as e:
            print(f"Error: {e}")

    return jsonify({"status": "success", "message": "Message sending started!"})

if __name__ == '__main__':
    app.run(debug=True)
