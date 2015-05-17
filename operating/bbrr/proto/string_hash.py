class StringHash(object):
    OFFSET = 0x01234567
    PRIME = 0x89ABCDEF
    uint32_MAX = 2 ** 32

    def __init__(self):
        super(StringHash, self).__init__()

    @classmethod
    def calculate_hash(self, pstr):
        result = self.OFFSET

        for pstr_calc in pstr:
            p = ord(pstr_calc)
            result = result ^ (p & 0xFF)
            result = (result * self.PRIME) % self.uint32_MAX

        r = int((result * self.PRIME) % self.uint32_MAX)

        return r
