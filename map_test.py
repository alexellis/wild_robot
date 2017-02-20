from map import *
import unittest

class map_test(unittest.TestCase):
	def test_map_val(self):
		map1 = map(
			{"max": -0.99,"min": 1.0}, 
			{"min":0, "max":100})
		self.assertEquals(map1.map_value(1.0), 0)
	def test_map_val_min(self):
		map1 = map(
			{"max": -0.99,"min": 1.0}, 
			{"min":0, "max":100})
		self.assertEquals(map1.map_value(-0.99), 100)
	def test_map_val_mid(self):
		map1 = map(
			{"max": -0.99,"min": 1.0}, 
			{"min":0, "max":100})
		self.assertEquals(round( map1.map_value(0.0)), 50)

	def test_(self):
                map1 = map(
                        {"max": 100,"min": 0},
                        {"min":180, "max":180})

		mapped = map1.()
		mapped = {
			"direction": "forwards"
		}
		self.assertEquals("forwards", mapped["direction"])

if(__name__=='__main__'):
	unittest.main()
