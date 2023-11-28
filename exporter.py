import prometheus_client
from flask import Response, Flask
from gevent import pywsgi
from prom_metrics import *
from collecter import metics
from arguments import get_args

app = Flask(__name__)

@app.route('/')
def index():
    return  "<h1>OceanStore 9000 Metrics!</h1><br> <a href='metrics'>Metrics</a>"

@app.route('/metrics')
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
