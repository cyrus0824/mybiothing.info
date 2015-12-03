# -*- coding: utf-8 -*-
from ${src_package}.api.handlers import FieldsHandler, ${query_handler_name}Handler, MetaDataHandler, ${annotation_handler_name}Handler, StatusHandler
import ${src_package}.settings.all_settings as all_settings

class ${settings_class}():
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

    def _status_check_id(self):
        return all_settings.STATUS_CHECK_ID

    def _return_applist(self):
        ret = [
            (r"/status", StatusHandler),
            (r"/metadata", MetaDataHandler),
            (r"/metadata/fields", FieldsHandler),        
        ]
        if self._api_version():
            ret += [
                (r"/" + self._api_version() + "/" + self._annotation_endpoint() + "/(.+)/?", ${annotation_handler_name}Handler),  # for get request
                (r"/" + self._api_version() + "/" + self._annotation_endpoint() + "/?$$", ${annotation_handler_name}Handler),            # for post request
                (r"/" + self._api_version() + "/" + self._query_endpoint() + "/?", ${query_handler_name}Handler),             
                (r"/" + self._api_version() + "/metadata", MetaDataHandler),
                (r"/" + self._api_version() + "/metadata/fields", FieldsHandler),
            ]
        else:
            ret += [
                (r"/" + self._annotation_endpoint() + "/(.+)/?", ${annotation_handler_name}Handler),  # for get request
                (r"/" + self._annotation_endpoint() + "/?$$", ${annotation_handler_name}Handler),            # for post request
                (r"/" + self._query_endpoint() + "/?", ${query_handler_name}Handler),
            ]
        return ret

