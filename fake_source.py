class fake_source:
	def __init__(self, selections):
		self.selections=selections

	def get_button(self, id):
		button_id=str(id)
		for key in self.selections.keys():
			if key == button_id:
				return self.selections[key]
		return 0
