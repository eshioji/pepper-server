from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from pepper_rest import app
import os

http_server = HTTPServer(WSGIContainer(app))
port = int(os.environ.get('PORT'))
http_server.listen(port)
IOLoop.instance().start()
