import argparse
import time
from datetime import datetime
import time
import string
import socket


SEED_VALUES = [0xe08a]
MAX_DOMAINS = 200
FREQUENCY = 7
TLDS = [".net", ".org", ".top"]
ACTOR = 'QADARS'


def getIP(d):
    try:
        data = socket.gethostbyname_ex(d)
        ip = repr(data[2])
        return ip
    except Exception:
        return False

class dga:
    def __init__(self, date, seed):
        self.date = date
        self.seed = seed
        self.domains = []
        self.charset = string.ascii_lowercase + string.digits
        self.generate_domains()

    def generate_domains(self):

        unixTime = int(time.mktime(self.date.timetuple()))
        dayOffset1 = 4*24*3600  #345600
        dayOffset2 = 7*24*3600  #604800
        #r = (unixTime - dayOffset1) * dayOffset2
        r = ((unixTime//dayOffset2)*dayOffset2 + dayOffset1)
        for i in range(MAX_DOMAINS):
            domain = "" 
            for _ in range(12):
                r = self.rand(r, self.seed)
                domain += self.charset[r % len(self.charset)]
            r = self.rand(r, self.seed)
            domain += TLDS[r % 3]
            self.domains.append(domain)

    def rand(self, r, seed):
        return  (seed - 1043968403*r) & 0x7FFFFFFF

    def getDomains(self):
        return self.domains

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", help="date for which to generate domains")
    args = parser.parse_args()

    if args.date:
        d = datetime.strptime(args.date, "%Y-%m-%d")
    else:
       d = datetime.now()

    dga = dga(d, 0xe08a)
    for domain in dga.getDomains():
        ip = getIP(domain)
        if ip:
            print(domain, ip)
        else:
            print(domain, "n/a")