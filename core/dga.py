class dga(object):
	"""
	Base DGA object
	"""
	def __init__(self):
		self.date = None
		self.seed = None
		self.domains = []
	
	def setDate(self, d):
		self.date = d

	def setSeed(self, s):
		self.seed = s

	def getDomains(self):
		return domains

	def generateDomains(self):
		pass