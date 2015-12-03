# -*- coding: utf-8 -*-
from biothings.www.api.handlers import MetaDataHandler, BiothingHandler, QueryHandler, StatusHandler, FieldsHandler
from ${src_package}.api.es import ESQuery
from ${src_package}.settings.example_settings import ${settings_class}
from ${src_package}.settings.ga_settings import GoogleAnalyticsSettings

class ${annotation_handler_name}Handler(BiothingHandler):
    ''' This class is for the ${annotation_endpoint} endpoint. '''
    esq = ESQuery()
    settings = ${settings_class}()
    ga_settings = GoogleAnalyticsSettings()

class ${query_handler_name}Handler(QueryHandler):
    ''' This class is for the ${query_endpoint} endpoint. '''
    esq = ESQuery()
    settings = ${settings_class}()
    ga_settings = GoogleAnalyticsSettings()

class StatusHandler(StatusHandler):
    ''' This class is for the /status endpoint. '''
    esq = ESQuery()
    settings = ${settings_class}()
    ga_settings = GoogleAnalyticsSettings()

class FieldsHandler(FieldsHandler):
    ''' This class is for the /metadata/fields endpoint. '''
    esq = ESQuery()
    settings = ${settings_class}()
    ga_settings = GoogleAnalyticsSettings()
    
class MetaDataHandler(MetaDataHandler):
    ''' This class is for the /metadata endpoint. '''
    esq = ESQuery()
    settings = ${settings_class}()
    ga_settings = GoogleAnalyticsSettings()