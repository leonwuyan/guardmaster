from detection.models import Tabel
from guardmaster import common as Common
from datetime import date, datetime

# COL_TYPE_LIST is related with ValueFormat(value_format.py)


class ValueFormat(object):
    def __init__(self, format_list, panel):
        super(ValueFormat, self).__init__()
        self.panel = panel
        self.format_list = format_list
        self.channel_list = None
        self.zone_list = None

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
            self.channel_list = Tabel.get_list(self.panel, Common.CHANNEL_LIST)
        ret = filter(lambda x: x.get('ChannelID') == id, self.channel_list)
        return ret[0].get('ChNm', Common.CHANNEL_ERROR)

    def _zone_list(self, id):
        if self.zone_list is None:
            self.zone_list = Tabel.get_list(self.panel, Common.ZONE_LIST)
        ret = filter(lambda x: x.get('ZoneID') == id, self.zone_list)
        return ret[0].get('ZoneNm', Common.ZONE_ERROR)

    def _identity(self, x):
        return x

    def _f_v(self, f, v):
        func = getattr(self, '_'+f, self._identity)
        try:
            ret = func(v)
        except Exception as e:
            ret = Common.FORMAT_ERROR
            print 'Exception :', e
        return ret

    def _fs_vs(self, fs, vs):
        ret = ()
        for i in range(len(vs)):
            ret = ret + (self._f_v(fs[i], vs[i]),)
        return ret

    def execute(self, vals):
        return map(lambda x: self._fs_vs(self.format_list, x), vals)
