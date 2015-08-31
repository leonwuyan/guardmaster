class Version(object):
    def __init__(self, a, b, c, d):
        self.version = [str(a), str(b), str(c), str(d)]

    def __str__(self):
        ret = '.'.join(self.version)
        return ret

    def __len__(self):
        return len(self.version)

    def __getitem__(self, index):
        try:
            return self.version[index]
        except:
            return '0'

    def __setitem__(self, index, value):
        self.version[index] = value

    def __lt__(self, obj):
        for i in range(len(self)):
            if int(self[i]) > int(obj[i]):
                return False
            if int(self[i]) < int(obj[i]):
                return True
        return False

    def __gt__(self, obj):
        for i in range(len(self)):
            if int(self[i]) > int(obj[i]):
                return True
            if int(self[i]) < int(obj[i]):
                return False
        return False

    def __le__(self, obj):
        return not self > obj

    def __ge__(self, obj):
        return not self < obj

    def __eq__(self, obj):
        for i in range(len(self)):
            if int(self[i]) != int(obj[i]):
                return False
        return True

    def __ne__(self, obj):
        return not self == obj

    def next(self):
        tmp = Version(self[0], self[1], self[2], self[3])
        tmp[3] = str(int(tmp[3]) + 1)
        return str(tmp)

    def is_app(self):
        if self[3] == '0':
            return True
        else:
            return False
