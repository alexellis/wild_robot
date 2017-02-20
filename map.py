class map:
	def __init__(self, range1, range2):
		self.range1=range1
		self.range2=range2
	def map_value(self, oldVal):
		old = self.range1["max"] - self.range1["min"]
		new = self.range2["max"] - self.range2["min"]
		return ((( oldVal - self.range1["min"]) * new) / old) + self.range2["min"]
#		return oldVal - (((self.range1["min"]) * new) / old) + self.range2["min"]

