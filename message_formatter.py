class message_formatter:
	def pad(self, val):
		out = str(val);

		if(val < 10):
			out = "00" + out
		elif(val < 100):
			out = "0" + out
		return out

	def keys(self):
		return ["arm","grip","IN1_L","IN2_L","IN3_R","IN4_R","EN_L","EN_R"]

	def valid(self, bag):
		keys = self.keys()
		for key in keys:
			if(bag.has_key(key)==False):
				return False
		return True

	def get_empty(self):
		bag={}
		keys = self.keys()
		for key in keys:
			bag[key]=0
		return bag

	def format(self, bag):
		st = "#"

		st += self.pad(bag["arm"])
		st += ","
		st += self.pad(bag["grip"])
		st += ","
		st += self.pad(bag["IN1_L"])
		st += ","
		st += self.pad(bag["IN2_L"])
		st += ","
		st += self.pad(bag["IN3_R"])
		st += ","
		st += self.pad(bag["IN4_R"])
		st += ","
		st += self.pad(bag["EN_L"])
		st += ","
		st += self.pad(bag["EN_R"])
		return st
