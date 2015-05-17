# conding:utf-8

import xinge
import json


class XgNotification(object):
    IOS = 'ios'
    ANDROID = 'android'

    def __init__(self, platform):
        super(XgNotification, self).__init__()
        if platform == self.IOS:
            self.secret_key = '5edb5710efe342308359e804e9775c0a'
            self.access_id = 2200097146
        if platform == self.ANDROID:
            self.secret_key = '809955837fd95d30f1b121d476b7434f'
            self.access_id = 2100080054
        self.platform = platform
        self.xg = xinge.XingeApp(self.access_id, self.secret_key)

    def build_msg(self, content, title=None):
        if self.platform == self.IOS:
            msg = xinge.MessageIOS()
            msg.alert = content
            msg.expireTime = 60 * 60 * 72
            # msg.sendTime = '2015-05-05 10:55:00'
            # msg.custom = {'aaa':'111', 'bbb':{'b1':1, 'b2':2}}
            # ti1 = xinge.TimeInterval(9, 30, 11, 30)
            # ti2 = xinge.TimeInterval(14, 0, 17, 0)
            # msg.acceptTime = (ti1, ti2)
        if self.platform == self.ANDROID:
            msg = xinge.Message()
            msg.type = xinge.Message.TYPE_NOTIFICATION
            msg.title = title
            msg.content = content
            msg.expireTime = 60 * 60 * 72
            # msg.sendTime = '2015-05-05 10:55:00'
            # msg.custom = {'aaa':'111', 'bbb':{'b1':1, 'b2':2}}
            # msg.multiPkg = 1
            # ti1 = xinge.TimeInterval(9, 30, 11, 30)
            # ti2 = xinge.TimeInterval(14, 0, 17, 0)
            # msg.acceptTime = (ti1, ti2)

        return msg

    def push_all_devices(self, msg):
        if self.platform == self.IOS:
            ret = self.xg.PushAllDevices(0, msg, xinge.XingeApp.ENV_DEV)
        if self.platform == self.ANDROID:
            ret = self.xg.PushAllDevices(0, msg, 0)
        return ret

    def push_tags(self, msg, tag_list):
        if self.platform == self.IOS:
            ret = self.xg.PushTags(
                0,
                tag_list,
                'AND',
                msg, xinge.XingeApp.ENV_DEV)
        if self.platform == self.ANDROID:
            ret = self.xg.PushTags(0, tag_list, 'AND', msg, 0)
        return ret

    def query_device_count(self):
        ret = self.xg.QueryDeviceCount()
        return ret

    def quert_push_status(self, id_list):
        ret = self.xg.QueryPushStatus(id_list)
        return ret

    def quert_tags(self, start=0, limit=100):
        ret = self.xg.QueryTags(start, limit)
        return ret

    def query_tag_token_num(self, tag):
        ret = self.xg.QueryTagTokenNum(tag)
        return ret
