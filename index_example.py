# -*- coding: utf-8 -*-
# Simple template example used to instantiate a new biothing API
from mybiothing.www.index_base import main
from mybiothing.www.api.handlers import QueryHandler, BiothingHandler, StatusCheckHandler, FieldsHandler

class DiseaseHandler(BiothingHandler):
    pass

APP_LIST = [
    (r"/status", StatusCheckHandler),
    (r"/metadata", MetaDataHandler),
    (r"/metadata/fields", FieldsHandler),
    (r"/disease/(.+)/?", DiseaseHandler),   # for annotation get request
    (r"/disease/?$", DiseaseHandler),       # for annotation post request
    (r"/query/?", QueryHandler),            # for query get/post request
]

if __name__ == '__main__':
    main(APP_LIST)
