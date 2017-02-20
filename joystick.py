import pygame
import sys
from joystick_reader import *

class ps3:
	def __init__(self, port):
		self.port=port

		pygame.init()
		pygame.joystick.init()
		self.joystick1 = pygame.joystick.Joystick(port)

	def connect(self):
		self.joystick1.init()

	def pump(self):
		pygame.event.pump()

	def get_buttons(self, debug=False):
		self.pump()
		jreader = joystick_reader(self.joystick1)
		return jreader.read()
	def read_axes(self):
		self.pump()
		jreader = joystick_reader(self.joystick1)
		return jreader.read_axes()
if(__name__=='__main__'):
	import time
        ps=ps3(0)
        ps.connect()
        while(True):
                ps.pump()
                b=ps.get_buttons(debug=True)
                print b

		a = ps.read_axes()
		print a

		time.sleep(0.5)


