from django.utils.translation import ugettext as _
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from detection.models import Tabel, Panel
from guardmaster import common as Common
from datetime import date, datetime
import logging

# COL_TYPE_LIST is related with ValueFormat(value_format.py)


class ValueFormat(object):
    def __init__(self, format_list, panel_id):
        super(ValueFormat, self).__init__()
        self.panel_id = panel_id
        self.format_list = format_list
        self.channel_list = None
        self.zone_list = None
        self.pay_channel_list = None
        self.chat_type_list = None
        self.user_status_list = None
        self.server_id = '0'

    def _date(self, d):
        if d.__class__ is date:
            return d.strftime('%Y-%m-%d')
        else:
            return Common.DATE_FORMAT_ERROR

    def _time(self, d):
        if d.__class__ is datetime:
            return d.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return Common.TIME_FORMAT_ERROR

    def _timestamp_to_date(self, timestamp):
        return self._date(datetime.fromtimestamp(long(timestamp)))

    def _timestamp_to_time(self, timestamp):
        return self._time(datetime.fromtimestamp(long(timestamp)))

    def _float_two(self, f):
        f = float(f)
        return str(round(f, 2))

    def _ratio_two(self, f):
        f = float(f) * 100
        return str(round(f, 2)) + '%'

    def _channel_list(self, id):
        if self.channel_list is None:
            self.channel_list = Tabel.get_enum(self.panel_id, Common.E_CHANNELID)
        return Common.filter_enum(self.channel_list, int(id), id)

    def _zone_list(self, id):
        if self.zone_list is None:
            self.zone_list = Tabel.get_enum(self.panel_id, Common.E_ZONEID)
        return Common.filter_enum(self.zone_list, int(id), id)

    def _identity_str(self, x):
        return str(x)

    def _identity(self, x):
        return x

    def _contact_reply(self, x):
        url = reverse('operating:contact_reply', args=(self.panel_id, x,))
        reply = _("reply")
        button = "<a href='" + url + "'>" + reply + "</a>"
        return button

    def _kick_ban(self, x):
        url = reverse('operating:change_single', args=(self.panel_id, 'single_query', 'kick_ban'))
        ban = _("ban")
        x = str(x)
        button = "<a href='javascript:management.kickbanUser(\"" + url + "\", \"" + self.server_id + "\", \"" + x + "\")'>" + ban + "</a>"
        return button

    def _ip_to_server(self, x):
        panel = get_object_or_404(Panel, pk=self.panel_id)
        Server = panel.server_set.get(ip=x)
        return Server.label

    def _pay_channel_list(self, id):
        if self.pay_channel_list is None:
            self.pay_channel_list = Tabel.get_enum(self.panel_id, Common.E_PAYCHANNEL)
        return Common.filter_enum(self.pay_channel_list, int(id), id)

    def _chat_type_list(self, id):
        if self.chat_type_list is None:
            self.chat_type_list = Tabel.get_enum(self.panel_id, Common.E_CHATTYPE)
        return Common.filter_enum(self.chat_type_list, int(id), id)

    def _user_status_list(self, id):
        if self.user_status_list is None:
            self.user_status_list = Tabel.get_enum(self.panel_id, Common.E_USERSTATUS)
        return Common.filter_enum(self.user_status_list, int(id), id)

    def _f_v(self, f, v):
        if f is None:
            f = ''
        func = getattr(self, '_'+f, self._identity)
        try:
            ret = func(v)
        except Exception as e:
            ret = Common.FORMAT_ERROR
            logger = logging.getLogger(__name__)
            logger.error('[' + func.__name__ + '] ' + str(e))
        return ret

    def _fs_vs(self, fs, vs):
        ret = ()
        for i in range(len(vs)):
            ret = ret + (self._f_v(fs[i], vs[i]),)
        return ret

    def execute(self, vals):
        return map(lambda x: self._fs_vs(self.format_list, x), vals)

    def set_server_id(self, server_id):
        self.server_id = str(server_id)
