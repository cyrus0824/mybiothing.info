'''
A thin python layer for accessing MyVariant ElasticSearch host.

Currently available URLs:

    /v1/query?q=rs58991260            variant query service
    /v1/variant/<variant_id>    variant annotation service

'''
import sys
import os.path
#import subprocess
#import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.escape
from tornado.options import define, options

src_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
if src_path not in sys.path:
    sys.path.append(src_path)
#from config import INCLUDE_DOCS

from www.api.es import ESQuery
from www.api.handlers import MetaDataHandler
from www.api.handlers import FieldsHandler

__USE_WSGI__ = False
#DOCS_STATIC_PATH = os.path.join(src_path, 'docs/_build/html')
#if INCLUDE_DOCS and not os.path.exists(DOCS_STATIC_PATH):
#    raise IOError('Run "make html" to generate sphinx docs first.')
STATIC_PATH = os.path.join(src_path, 'www/static')

define("port", default=8000, help="run on the given port", type=int)
define("address", default="127.0.0.1", help="run on localhost")
define("debug", default=False, type=bool, help="run in debug mode")
tornado.options.parse_command_line()
if options.debug:
    import tornado.autoreload
    import logging
    logging.getLogger().setLevel(logging.DEBUG)
    options.address = '0.0.0.0'


class StatusCheckHandler(tornado.web.RequestHandler):
    ''' Handles requests to check the status of the server. '''
    def head(self):
        esq = ESQuery()
        esq = esq.get_status_check()

    def get(self):
        self.head()
        self.write('OK')

APP_LIST = [
    (r"/status", StatusCheckHandler),
    (r"/metadata", MetaDataHandler),
    (r"/metadata/fields", FieldsHandler),
]

settings = {}
if options.debug:
    # from config import STATIC_PATH
    settings.update({
        "static_path": STATIC_PATH,
    })
    # from config import auth_settings
    # settings.update(auth_settings)


def main(APP_LIST):
    application = tornado.web.Application(APP_LIST, **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port, address=options.address)
    loop = tornado.ioloop.IOLoop.instance()
    if options.debug:
        tornado.autoreload.start(loop)
        tornado.autoreload.watch(os.path.join(STATIC_PATH, 'index.html'))
        logging.info('Server is running on "%s:%s"...' % (options.address, options.port))

    loop.start()