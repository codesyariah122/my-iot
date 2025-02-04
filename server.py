from flask import Flask, request, jsonify

app = Flask(__name__)

parkir_status = "empty"

@app.route('/update', methods=['POST'])
def update_status():
    global parkir_status
    data = request.get_json()

    if 'status' in data:
        parkir_status = data['status']
        return jsonify({"message": "Status updated", "status": parkir_status})
    else:
        return jsonify({"error": "Invalid data"}), 400

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({"status": parkir_status})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
