from core.dga import dga

MAX_DOMAINS = 150

class vawtrak_dga(dga):
	def setTld(seld, tld):
		self.tld = tld

	def generateDomains(self):
		if self.seed == None:
			raise Exception("Seed value not set")
			return
		for x in range(0x96):
			domain = ""
			length = self.rand() %5 +7
			for i in range(length):
				domain += chr(self.rand() %26 + 0x61)
			domain += ("." + self.tld)
			self.domains.append(domain)

	def rand(self):
		self.seed = ((self.seed * 0x41c64e6d) + 0x3039) & 0xffffffff
		return self.seed
