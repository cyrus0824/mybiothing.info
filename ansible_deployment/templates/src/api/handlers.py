# -*- coding: utf-8 -*-
from mybiothing.www.api.handlers import MetaDataHandler, BiothingHandler, QueryHandler, StatusHandler, FieldsHandler
from {{ src_package }}.api.es import ESQuery
from {{ src_package }}.settings.example_settings import My{{ cap_src_package }}Settings
from {{ src_package }}.settings.ga_settings import GoogleAnalyticsSettings

class MetaDataHandler(MetaDataHandler):
    esq = ESQuery()
    settings = My{{ cap_src_package }}Settings()
    ga_settings = GoogleAnalyticsSettings()
    pass

class {{ cap_src_package }}Handler(BiothingHandler):
    esq = ESQuery()
    settings = My{{ cap_src_package }}Settings()
    ga_settings = GoogleAnalyticsSettings()
    pass

class QueryHandler(QueryHandler):
    esq = ESQuery()
    settings = My{{ cap_src_package }}Settings()
    ga_settings = GoogleAnalyticsSettings()
    pass

class StatusHandler(StatusHandler):
    esq = ESQuery()
    settings = My{{ cap_src_package }}Settings()
    ga_settings = GoogleAnalyticsSettings()
    pass

class FieldsHandler(FieldsHandler):
    esq = ESQuery()
    settings = My{{ cap_src_package }}Settings()
    ga_settings = GoogleAnalyticsSettings()
    pass
