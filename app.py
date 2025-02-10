from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Hello from VM 1 (Microservice Server)!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
