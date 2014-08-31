import flask
from pyformance import registry
from pyformance.registry import time_calls
from pyformance import timer
from werkzeug.exceptions import BadRequest
from flask import request
import simplejson as json


app = flask.Flask(__name__, static_url_path='') 
app.config['DEBUG'] = True

@app.route('/')
def root():
    return app.send_static_file('index.html')



def format_response(stuff):
    return {'resp': stuff}


@app.route('/api/<something_id>', methods=['GET'])
def something(something_id):
    return flask.jsonify(format_response({"hey": something_id, "huh": { "yay": 2}}))



@app.route('/metrics', methods=['GET'])
def metrics():
    return flask.jsonify(registry.dump_metrics())

# Only for testing
if __name__ == '__main__':
    app.run()
