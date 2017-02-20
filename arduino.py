import serial
from datetime import datetime
import sys
import time

from message_formatter import *

class wildserial:
	def quit(self):
		self.ser.close()
	def __init__(self,interface):
		self.interface=interface
		self.ser=self.setup()
	def setup(self):
		ser = serial.Serial('/dev/tty'+self.interface, 9600)
		return ser

	def stop(self):
		self.ser.write('p')

	def go(self, direction,speed,duration):
		if(direction== 'forwards'):
			self.ser.write('w')
		if(direction== 'reverse'):
			self.ser.write('s')
		if(direction== 'right'):
			self.ser.write('a')
		if(direction== 'left'):
			self.ser.write('d')


class wild_multi_serial:
	def quit(self):
		self.ser.close()
	def __init__(self,interface):
		self.interface=interface
		self.ser=self.setup()
		self.lastMsg=None

	def setup(self):
		ser = serial.Serial('/dev/tty'+self.interface, 9600,timeout=0.025)
		return ser

	def read(self):
		return self.ser.readlines()

	def stop(self,arm_pos, grip_pos):
		m = message_formatter()
		bag = m.get_empty()
		bag["grip"] = grip_pos
		bag["arm"]=arm_pos
		self.write(m.format(bag))

	def set_probe_position(self,arm_pos, grip_pos):
		m = message_formatter()
		bag = m.get_empty()
		bag["grip"] = grip_pos
		bag["arm"]=arm_pos
		self.write(m.format(bag))	

	def go(self, direction, speed, arm_pos, grip_pos):
		m = message_formatter()
		bag = m.get_empty()
		if(direction== 'forwards'):
			bag["IN2_L"] = 1
			bag["IN4_R"] = 1
			bag["EN_L"] = speed
			bag["EN_R"] = speed
		if(direction== 'reverse'):
			bag["IN1_L"] = 1
			bag["IN3_R"] = 1
			bag["EN_L"] = speed
			bag["EN_R"] = speed
		if(direction== 'right'):
			bag["IN1_L"] = 1
			bag["IN4_R"] = 1
			bag["EN_L"] = speed
			bag["EN_R"] = speed
		if(direction== 'left'):
			bag["IN2_L"] = 1
			bag["IN3_R"] = 1
			bag["EN_L"] = speed
			bag["EN_R"] = speed

		bag["grip"] = grip_pos
		bag["arm"]=arm_pos
		print str(speed)
		self.write(m.format(bag))

	def write(self, msg):
		if(self.lastMsg is None or msg != self.lastMsg):
			print msg
			self.ser.write(msg)
			self.lastMsg=msg
