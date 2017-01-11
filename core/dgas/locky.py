from datetime import datetime
from core.dga import dga

MAX_DOMAINS = 12
TLDS = ['ru', 'info', 'biz', 'click', 'su', 'work', 'pl', 'org', 'pw', 'xyz']

def ror32(v, s):
    v &= 0xFFFFFFFF
    return ((v >> s) | (v << (32-s))) & 0xFFFFFFFF

def rol32(v, s):
    v &= 0xFFFFFFFF
    return ((v << s) | (v >> (32-s))) & 0xFFFFFFFF


class locky_dga(dga):
    def generateDomains(self):
        for i in range(12):
            self.domains.append(self.genDomain(i))
        
    def genDomain(self, domain_nr): 
        shift = 7
        seed_shifted = rol32(self.seed, 17)
        dnr_shifted = rol32(domain_nr, 21)
    
        k = 0
        year = self.date.year
        for _ in range(7):
            t_0 = ror32(0xB11924E1 * (year + k + 0x1BF5), shift) & 0xFFFFFFFF
            t_1 = ((t_0 + 0x27100001) ^ k) & 0xFFFFFFFF
            t_2 = (ror32(0xB11924E1 * (t_1 + self.seed), shift)) & 0xFFFFFFFF
            t_3 = ((t_2 + 0x27100001) ^ t_1) & 0xFFFFFFFF
            t_4 = (ror32(0xB11924E1 * (self.date.day//2 + t_3), shift)) & 0xFFFFFFFF
            t_5 = (0xD8EFFFFF - t_4 + t_3) & 0xFFFFFFFF
            t_6 = (ror32(0xB11924E1 * (self.date.month + t_5 - 0x65CAD), shift)) & 0xFFFFFFFF
            t_7 = (t_5 + t_6 + 0x27100001) & 0xFFFFFFFF
            t_8 = (ror32(0xB11924E1 * (t_7 + seed_shifted + dnr_shifted), shift)) & 0xFFFFFFFF
            k = ((t_8 + 0x27100001) ^ t_7) & 0xFFFFFFFF
            year += 1

        length = (k % 11) + 7
        domain = ""
        for i in range(length):
            k = (ror32(0xB11924E1*rol32(k, i), shift) + 0x27100001) & 0xFFFFFFFF
            domain += chr(k % 25 + ord('a'))

        domain += '.'
        k = ror32(k*0xB11924E1, shift)
        tld_i = ((k + 0x27100001) & 0xFFFFFFFF) % len(TLDS)
        domain += self.tlds[TLDS]
        return domain

