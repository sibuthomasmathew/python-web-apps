"""Demo"""

import socket
from datetime import datetime
from flask import Flask


app = Flask(__name__, instance_relative_config=True)


def html_rendering(data: str) -> str:
    """Function to generate HTML tags"""

    return f"<html><body><h1>{data}</h1></body></html>\n"


@app.route('/time')
def timestamp():
    """Function to return timestamp"""

    return html_rendering(str(datetime.now()))


@app.route('/hostname')
def hostname():
    """Function to return server hostname"""

    return html_rendering(socket.gethostname())


@app.route('/health')
def health_check():
    """Function to respond to health check probes"""

    return "OK"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
