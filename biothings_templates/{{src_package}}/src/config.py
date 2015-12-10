# -*- coding: utf-8 -*-
from www.api.handlers import FieldsHandler, ${query_handler_name}Handler, MetaDataHandler, ${annotation_handler_name}Handler, StatusHandler

# *****************************************************************************
# Elasticsearch variables
# *****************************************************************************

# elasticsearch server transport url
ES_HOST = 'localhost:9200'
# elasticsearch index name
ES_INDEX_NAME = '${src_package}_current'
# elasticsearch document type
ES_DOC_TYPE = '${es_doctype}'

# *****************************************************************************
# Google Analytics Settings
# *****************************************************************************

# Google Analytics Account ID
GA_ACCOUNT = ''
# Turn this to True to start google analytics tracking
RUN_IN_PROD = False

# 'category' in google analytics event object
GA_EVENT_CATEGORY = 'v1_api'
# 'action' for get request in google analytics event object
GA_EVENT_GET_ACTION = 'get'
# 'action' for post request in google analytics event object
GA_EVENT_POST_ACTION = 'post'

# *****************************************************************************
# URL settings
# *****************************************************************************

# For URL stuff
ANNOTATION_ENDPOINT = '${annotation_endpoint}'
QUERY_ENDPOINT = '${query_endpoint}'
API_VERSION = 'v1'
# TODO Fill in a status id here
STATUS_CHECK_ID = ''

# *****************************************************************************
# Settings class
# *****************************************************************************

class ${settings_class}():
    def __init__(self):
        pass

    def _annotation_endpoint(self):
        return ANNOTATION_ENDPOINT

    def _query_endpoint(self):
        return QUERY_ENDPOINT

    def _api_version(self):
        if API_VERSION:
            return API_VERSION
        else:
            return ''

    def _status_check_id(self):
        return STATUS_CHECK_ID

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

    def event_for_get_action(self):
        return GA_EVENT_GET_ACTION

    def event_for_post_action(self):
        return GA_EVENT_POST_ACTION

    def event_category(self):
        return GA_EVENT_CATEGORY

    def ga_event_object(self, endpoint, action, data):
        ret = {}
        ret['category'] = self.event_category()
        if action == 'GET':
            ret['action'] = '_'.join([endpoint, self.event_for_get_action()])
        elif action == 'POST':
            ret['action'] = '_'.join([endpoint, self.event_for_post_action()])
        for (k,v) in data.items():
            ret['label'] = k
            ret['value'] = v
        return ret


