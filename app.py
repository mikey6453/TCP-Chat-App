from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

messages = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    msg_data = request.json
    nickname = msg_data.get('nickname')
    message = msg_data.get('message')
    messages.append(f"{nickname}: {message}")
    return jsonify(success=True)

@app.route('/get_messages')
def get_messages():
    return jsonify(messages=messages)

if __name__ == '__main__':
    app.run(debug=True, port=55556)