from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/vector/voice_command', methods=["POST"])
def get_voice_command():
    data = request.get_json()
    voice_message = data.get("voice_message")

    if not voice_message:
        return jsonify({'error': 'No message provided'}), 400

    print(f"Received message: {voice_message}")

    return jsonify({"received_message": voice_message}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)