from flask import Flask, render_template
import socket
from datetime import datetime, timezone

app = Flask(__name__)


@app.route("/")
def home():
    server_hostname = socket.gethostname()
    current_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

    return render_template(
        "index.html",
        hostname=server_hostname,
        current_time=current_time
    )


@app.route("/health")
def health():
    return {
        "status": "healthy",
        "server": socket.gethostname()
    }, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)