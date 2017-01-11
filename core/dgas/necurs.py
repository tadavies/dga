from core.dga import dga
from datetime import datetime

TLDS = ['tj','in','jp','tw','ac','cm','la','mn','so','sh','sc','nu','nf','mu', 'ms','mx','ki','im','cx','cc','tv','bz','me','eu','de','ru','co','su','pw','kz','sx','us','ug','ir','to','ga','com','net','org','biz','xxx','pro','bit']

class necurs_dga(dga):

    def genDomain(self,sequence_nr):
        domain = ""
        n = self.pseudo_random(self.date.year)
        n = self.pseudo_random(n + self.date.month + 43690)
        n = self.pseudo_random(n + (self.date.day>>2))
        n = self.pseudo_random(n + sequence_nr)
        n = self.pseudo_random(n + self.seed)
        domain_length = self.mod64(n, 15) + 7
        for i in range(domain_length):
            n = self.pseudo_random(n+i) 
            ch = self.mod64(n, 25) + ord('a') 
            domain += chr(ch)
            n += 0xABBEDF
            n = self.pseudo_random(n) 
        tld = self.tlds[self.mod64(n, 43)]
        domain += '.' + tld
        return domain

    def generateDomains(self):
        if self.seed != None and self.date != None:
            for x in range(2048):
                self.domains.append(self.genDomain(x))
            return True
        return False

    def pseudo_random(self, value):
        loops = (value & 0x7F) + 21
        for index in range(loops):
            value += ((value*7) ^ (value << 15)) + 8*index - (value >> 5)
            value &= ((1 << 64) - 1)
        return value

    def mod64(self, nr1, nr2):
        return nr1 % nr2


