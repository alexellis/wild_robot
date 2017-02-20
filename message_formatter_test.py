from message_formatter import *
import unittest

class message_formatter_test(unittest.TestCase):

	def test_valid_returnsFalse_DuetoMissingKeys(self):
		bag = {
			"arm": 100,
			"grip": 110
		}
		m=message_formatter()
		self.assertEquals(False, m.valid(bag))

	def test_valid_returnsTrueAllKeysPresent(self):
		bag = {
			"arm": 0,
			"grip": 0,
			"IN1_L":0,
			"IN2_L":0,
			"IN3_R":0,
			"IN4_R":0,
		}
		m=message_formatter()
		self.assertEquals(True, m.valid(bag))

	def test_format_threedigit_string(self):
		bag = {
			"arm": 100,
			"grip": 110,
			"IN1_L":0,
			"IN2_L":0,
			"IN3_R":0,
			"IN4_R":0
		}
		m=message_formatter()
		self.assertEquals("#100,110,000,000,000,000", m.format(bag))

	def test_format_two_string(self):
		bag = {
			"arm": 10,
			"grip": 11,
			"IN1_L":0,
			"IN2_L":0,
			"IN3_R":0,
			"IN4_R":0
		}

		m=message_formatter()
		self.assertEquals("#010,011,000,000,000,000", m.format(bag))

	def test_format_zero_string(self):
		bag = {
			"arm": 0,
			"grip": 0,
			"IN1_L":0,
			"IN2_L":0,
			"IN3_R":0,
			"IN4_R":0
		}
		m=message_formatter()
		self.assertEquals("#000,000,000,000,000,000", m.format(bag))

if(__name__=='__main__'):
	unittest.main()