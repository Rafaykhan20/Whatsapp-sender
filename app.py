from flask import Flask, render_template, request, jsonify
import subprocess
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

    # Call the Node.js script
    try:
        subprocess.run([
            "node",
            "whatsapp_sender.js",  # Path to your Node.js script
            target_number,
            message_file_path,
            str(message_delay),
            hater_name
        ], check=True)
        return jsonify({"status": "success", "message": "Message sending started!"})
    except subprocess.CalledProcessError as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
