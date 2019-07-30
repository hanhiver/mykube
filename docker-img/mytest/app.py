from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    ip_add = socket.gethostbyname(hostname)
    return "Version: V2.0 from host: {} with IP: {} \n".format(hostname, ip_add)

if __name__ == '__main__':
    app.run(host="0.0.0.0")


