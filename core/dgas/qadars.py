from core.dga import dga
from datetime import datetime
import time
import string

SEED_VALUES = [0xe08a]
MAX_DOMAINS = 200
FREQUENCY = 7
TLDS = [".net", ".org", ".top"]

class qadars_dga(dga):
    def generateDomains(self):
        charset = string.ascii_lowercase + string.digits
        unixTime = int(time.mktime(self.date.timetuple()))
        dayOffset1 = 4*24*3600  #345600
        dayOffset2 = 7*24*3600  #604800
        r = ((unixTime//dayOffset2)*dayOffset2 + dayOffset1)
        for i in range(MAX_DOMAINS):
            domain = "" 
            for _ in range(12):
                r = self.rand(r, self.seed)
                domain += charset[r % len(charset)]
            r = self.rand(r, self.seed)
            domain += TLDS[r % 3]
            self.domains.append(domain)

    def rand(self, r, seed):
        return  (seed - 1043968403*r) & 0x7FFFFFFF



