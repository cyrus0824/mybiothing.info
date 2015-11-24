# -*- coding: utf-8 -*-
from myexample.api.handlers import FieldsHandler, QueryHandler, MetaDataHandler, ExampleHandler, StatusHandler
import settings.all_settings as all_settings

class MyExampleSettings():
    def __init__(self):
        pass

    def _annotation_endpoint(self):
        return all_settings.ANNOTATION_ENDPOINT

    def _query_endpoint(self):
        return all_settings.QUERY_ENDPOINT

    def _api_version(self):
        if all_settings.API_VERSION:
            return all_settings.API_VERSION
        else:
            return ''

    def _return_applist(self):
        ret = [
            (r"/status", StatusHandler),
            (r"/metadata", MetaDataHandler),
            (r"/metadata/fields", FieldsHandler),
            (r"/" self._api_version() + self._annotation_endpoint() + "/(.+)/?", ExampleHandler),   # for get request
            (r"/" + self._api_version() + self._annotation_endpoint() + "/?$", ExampleHandler),       # for post request
            (r"/" + self._api_version() + self._query_endpoint() + "/?", QueryHandler),            # for query get/post request
            ]
        if self._api_version():
            ret += [
            (r"/" + self._api_version() + "metadata", MetaDataHandler),        # for metadata requests
            (r"/" + self._api_version() + "metadata/fields", FieldsHandler),   # for available field information
            ]
        return ret
