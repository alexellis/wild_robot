import unittest
from joystick_reader import *

class joystick_reader_test(unittest.TestCase):
	def test_map_has_all_keys(self):
		s=fake_source()
		reader=joystick_reader(s)
		states=reader.read()

		keys=[
			'pad_left',
			'pad_right',
			'pad_up',
			'pad_down',
			'square',
			'cross',
			'push_left',
			'push_right',
			'right_trigger',
			'left_trigger',
			'right_shoulder',
			'left_shoulder'
		]

		for key in keys:
			self.assertEqual(False, states[key])			

if(__name__=='__main__'):
	unittest.main()