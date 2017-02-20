import serial
from datetime import datetime
import sys
import time

class wildserial:
	def quit(self):
		self.ser.close()

	def __init__(self,interface):
		self.interface=interface
		self.ser=self.setup()
	def setup(self):
		ser = serial.Serial('/dev/tty'+self.interface, 9600)
		return ser

	def go(self, direction,speed,duration):
		if(direction== 'forwards'):
			self.ser.write('w')
		if(direction== 'reverse'):
			self.ser.write('s')
		if(direction== 'right'):
			self.ser.write('a')
		if(direction== 'left'):
			self.ser.write('d')

		time.sleep(duration)
		# Park it
		self.ser.write('p')
