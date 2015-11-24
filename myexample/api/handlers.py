# -*- coding: utf-8 -*-
from mybiothing.www.api.handlers import MetaDataHandler, BiothingHandler, QueryHandler, StatusHandler, FieldsHandler
from myexample.api.es import ESQuery

class MetaDataHandler(MetaDataHandler):
    esq = ESQuery()
    pass

class ExampleHandler(BiothingHandler):
    esq = ESQuery()
    pass

class QueryHandler(QueryHandler):
    esq = ESQuery()
    pass

class StatusHandler(StatusHandler):
    esq = ESQuery()
    pass

class FieldsHandler(FieldsHandler):
    esq = ESQuery()
    pass
