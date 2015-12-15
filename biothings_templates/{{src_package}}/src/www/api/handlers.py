# -*- coding: utf-8 -*-
from biothings.www.api.handlers import MetaDataHandler, BiothingHandler, QueryHandler, StatusHandler, FieldsHandler
from www.api.es import ESQuery
import config

class ${annotation_handler_name}(BiothingHandler):
    ''' This class is for the /${annotation_endpoint} endpoint. '''
    settings = config.${settings_class}()
    esq = ESQuery(settings)

class ${query_handler_name}(QueryHandler):
    ''' This class is for the /${query_endpoint} endpoint. '''
    settings = config.${settings_class}()
    esq = ESQuery(settings)

class StatusHandler(StatusHandler):
    ''' This class is for the /status endpoint. '''
    settings = config.${settings_class}()
    esq = ESQuery(settings)

class FieldsHandler(FieldsHandler):
    ''' This class is for the /metadata/fields endpoint. '''
    settings = config.${settings_class}()
    esq = ESQuery(settings)

class MetaDataHandler(MetaDataHandler):
    ''' This class is for the /metadata endpoint. '''
    settings = config.${settings_class}()
    esq = ESQuery(settings)


def return_applist():
    return [
        (r"/${annotation_endpoint}/(.+)/?", ${annotation_handler_name}),
        (r"/${annotation_endpoint}/?$$", ${annotation_handler_name}),
        (r"/${query_endpoint}/?", ${query_handler_name}),
        (r"/status", StatusHandler),
        (r"/metadata", MetaDataHandler),
        (r"/metadata/fields", FieldsHandler),
    ]