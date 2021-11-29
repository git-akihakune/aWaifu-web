import os
import threading
from subprocess import Popen, PIPE, run
from . import log

def runServer():
    import flask
    app = flask.Flask(__name__)
    app.run(debug=True, use_reloader=False)

def stopServer(environ):
    if not 'werkzeug.server.shutdown' in environ:
        raise RuntimeError('Not running the development server')
    environ['werkzeug.server.shutdown']()

def debugServerTest() -> bool:
    log.notify("Trying to run debug server")
    try:
        assert not os.environ['FLASK_ENV'] and not os.environ['FLASK_DEBUG']
    except KeyError:
        log.failed("Environment variables FLASK_APP and FLASK_ENV not set")
        return False
    
    try:
        threading.Thread(runServer()).start()
        log.success("Debug server started")
        return True
    except Exception as e:
        log.failed("Debug server failed to start: {}".format(e))
        return False