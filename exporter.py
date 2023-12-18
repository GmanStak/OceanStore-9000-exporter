import prometheus_client
from flask import Response, Flask
from flask_basicauth import BasicAuth
from gevent import pywsgi
from prom_metrics import *
from collecter import metics
from arguments import get_args,get_auth

args = get_args()

auth_path = args.auth_config
auth_host,auth_passwd = get_auth(auth_path)

app = Flask(__name__)

app.config["BASIC_AUTH_USERNAME"] = auth_host
app.config["BASIC_AUTH_PASSWORD"] = auth_passwd
basic_auth = BasicAuth(app)



@app.route('/')
@basic_auth.required
def index():
    return  "<h1>OceanStore 9000 Metrics!</h1><br> <a href='metrics'>Metrics</a>"

@app.route('/metrics')
@basic_auth.required
def get_metrics():
    clear_metrics()
    metics()
    return Response(prometheus_client.generate_latest(REGISTRY),mimetype="text/plain")

if __name__=='__main__':
    args = get_args()
    host = args.address
    port = int(args.port)
    server = pywsgi.WSGIServer((host,port),app)
    server.serve_forever()
