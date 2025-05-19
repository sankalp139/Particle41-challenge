from flask import Flask, jsonify, request
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/')
def time_service():
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    return jsonify({
         "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "ip": client_ip     
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
