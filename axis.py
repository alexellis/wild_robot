
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

	def get_numaxes(self):
		return self.joystick1.get_numaxes()
	def get_axis(self, x):
		return self.joystick1.get_axis(x)


if(__name__=='__main__'):
	import time
        ps=ps3(0)
        ps.connect()
	print "Num axes"
	axes = ps.get_numaxes()
	print ps.get_numaxes()
        while(True):
                ps.pump()
		for x in xrange(axes):
			print str(x) + " " + str(ps.get_axis(x))
		time.sleep(0.5)


