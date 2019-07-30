from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def hello():
    hostname = socket.gethostname()
    ip_add = socket.gethostbyname(hostname)
    with open('/var/data/test.txt', 'r') as test_file:
        a = test_file.readline()

    with open('/var/data/ok.txt', 'w') as write_file:
        write_file.write('{}, {}, Veni, vid, vici!'.format(hostname, ip_add))

    return "{}: Version: V2.0 from host: {} with IP: {} \n".format(a, hostname, ip_add)

if __name__ == '__main__':
    app.run(host="0.0.0.0")


