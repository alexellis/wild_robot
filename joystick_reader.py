class joystick_reader:
	def __init__(self, buttonSrc):
		self.buttonSrc = buttonSrc
		self.map = {
			'select':0,
			'pad_left': 5,
			'pad_right': 7,
			'pad_up': 4,
			'pad_down': 6,
			'square': 15,
			'cross': 14,
			'push_left': 1,
			'push_right': 2,
			'right_trigger': 9,
			'left_trigger': 8,
			'right_shoulder': 11,
			'left_shoulder': 10
		}
		self.axisMap = {
			'leftright' : 0,
			'forwardbackwards' : 3
		}

	def read(self):
		mapped = {}
		for key in self.map.keys():

			button_id = self.map[key]

			mapped[key] = self.buttonSrc.get_button(button_id) == 1

		return mapped

	def read_axes(self):
		mapped = {}
		for axis in self.axisMap.keys():
			key = self.axisMap[axis]
			reading = self.buttonSrc.get_axis(key)
			mapped[axis] = reading
		return mapped

