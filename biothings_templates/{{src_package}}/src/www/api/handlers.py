# -*- coding: utf-8 -*-
from biothings.www.api.handlers import MetaDataHandler, BiothingHandler, QueryHandler, StatusHandler, FieldsHandler
from www.api.es import ESQuery
import config

class ${annotation_handler_name}Handler(BiothingHandler):
    ''' This class is for the /${annotation_endpoint} endpoint. '''
    esq = ESQuery()
    settings = config.${settings_class}()

class ${query_handler_name}Handler(QueryHandler):
    ''' This class is for the /${query_endpoint} endpoint. '''
    esq = ESQuery()
    settings = config.${settings_class}()

class StatusHandler(StatusHandler):
    ''' This class is for the /status endpoint. '''
    esq = ESQuery()
    settings = config.${settings_class}()

class FieldsHandler(FieldsHandler):
    ''' This class is for the /metadata/fields endpoint. '''
    esq = ESQuery()
    settings = config.${settings_class}()

class MetaDataHandler(MetaDataHandler):
    ''' This class is for the /metadata endpoint. '''
    esq = ESQuery()
    settings = config.${settings_class}()