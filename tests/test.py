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

def debugServerTest(runServer: bool = False) -> bool:
    log.notify("Trying to run debug server")
    try:
        assert os.environ['FLASK_APP'] and os.environ['FLASK_ENV']
        if not runServer:
            log.passed("Environment variables test passed")
            return True
    except KeyError:
        log.failed("Environment variables FLASK_APP and FLASK_ENV not set")
        return False
    except AssertionError:
        log.failed("Assertion failed: FLASK_APP and FLASK_ENV value not set")
        return False
    
    if runServer:
        try:
            threading.Thread(runServer()).start()
            log.passed("Debug server started")
            return True
        except Exception as e:
            log.failed("Debug server failed to start: {}".format(e))
            return False

def run():
    log.notify("Running automated tests")
    debugServerTest()