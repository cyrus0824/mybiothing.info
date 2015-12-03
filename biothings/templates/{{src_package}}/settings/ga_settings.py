# -*- coding: utf-8 -*-
import ${src_package}.settings.all_settings as settings

class GoogleAnalyticsSettings():
    def __init__(self):
        pass

    def event_for_get_action(self):
        return settings.GA_EVENT_GET_ACTION

    def event_for_post_action(self):
        return settings.GA_EVENT_POST_ACTION

    def event_category(self):
        return settings.GA_EVENT_CATEGORY

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
