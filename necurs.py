import socket
import argparse
from datetime import datetime

def pseudo_random(value):
    loops = (value & 0x7F) + 21
    for index in range(loops):
        value += ((value*7) ^ (value << 15)) + 8*index - (value >> 5)
        value &= ((1 << 64) - 1)
    return value

def mod64(nr1, nr2):
    return nr1 % nr2

class dga:
    def __init__(self, seed=None, date=None):
        self.seed = seed
        self.date = date
        self.domains = []
        self.tlds = ['tj','in','jp','tw','ac','cm','la','mn','so','sh','sc','nu','nf','mu',
                'ms','mx','ki','im','cx','cc','tv','bz','me','eu','de','ru','co','su','pw',
                'kz','sx','us','ug','ir','to','ga','com','net','org','biz','xxx','pro','bit']
        self.generateDomains()

    def genDomain(self,sequence_nr):
        domain = ""
        n = pseudo_random(self.date.year)
        n = pseudo_random(n + self.date.month + 43690)
        n = pseudo_random(n + (self.date.day>>2))
        n = pseudo_random(n + sequence_nr)
        n = pseudo_random(n + self.seed)
        domain_length = mod64(n, 15) + 7
        for i in range(domain_length):
            n = pseudo_random(n+i) 
            ch = mod64(n, 25) + ord('a') 
            domain += chr(ch)
            n += 0xABBEDF
            n = pseudo_random(n) 
        tld = self.tlds[mod64(n, 43)]
        domain += '.' + tld
        return domain

    def generateDomains(self):
        if self.seed != None and self.date != None:
            for x in range(2048):
                self.domains.append(self.genDomain(x))
            return True
        return False

    def getDomains(self):
        return self.domains

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--date", help="as YYYY-mm-dd")
    args = parser.parse_args()
    date_str = args.date
    if date_str:
        date = datetime.strptime(date_str, "%Y-%m-%d")
    else:
        date = datetime.now()
    seeds = [5,7,9,13]
    for s in seeds:
        obj = dga(s,date)
if __name__=="__main__":
    main()
