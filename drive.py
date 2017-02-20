import sys
import time
import subprocess
from joystick import ps3

from arduino import wild_multi_serial

rover = wild_multi_serial('USB0')
rover.setup()

time.sleep(1.5)
print "set up done. OK"
quit=False
turnTime=0.5
moveSpeed=125
moveTime=0.5
arm_pos=90
grip_pos = 90
turnSpeed = 145

MIN_SPEED = 80
MAX_SPEED = 230

MAX_GRIP = 170
MIN_GRIP = 20

select_hold_time = None

def drive(line):
	global arm_pos
	global moveTime
	print( "Command: " + line)

	if(line=='quit'):
		quit=True
		rover.quit()
	elif(line=='park'):
		rover.stop(arm_pos,grip_pos)
	elif(line=='forwards'):
		rover.go('forwards', moveSpeed,arm_pos,grip_pos)
	elif(line=='reverse'):
		rover.go('reverse', moveSpeed,arm_pos,grip_pos)
	elif(line=='left'):
		rover.go('left', turnSpeed,arm_pos,grip_pos)
	elif(line=='right'):
		rover.go('right', turnSpeed,arm_pos,grip_pos)
	elif(line=="set_probe"):
		rover.set_probe_position(arm_pos, grip_pos)
		time.sleep(0.01)

	# for line in rover.read():
	# 	print line

ps = ps3(0)
ps.connect()

def read_loop(last_buttons):
	global arm_pos
	global grip_pos
	global moveSpeed
	global turnSpeed
	global select_hold_time

	ps.pump()

	buttons = ps.get_buttons(False)
	
	if(buttons["left_trigger"]==True):
		drive("forwards")
	elif(buttons["right_trigger"]==True):
		drive("reverse")

	elif(buttons["select"] == False and select_hold_time!=None):
		select_hold_time = None
	elif(buttons["select"] == True):
		if(select_hold_time==None):
			select_hold_time = time.time()
		else:
			if(time.time() - select_hold_time > 5):
				subprocess.call("shutdown","-h","0")
				sys.exit()
				
	elif(buttons["pad_left"]==True):
		drive("right")
	elif(buttons["pad_right"]==True):
		drive("left")

	elif(buttons["pad_up"]==True):
		if(last_buttons==None or last_buttons["pad_up"] == False):
			print "turn increase"

			if(moveSpeed+10 <= MAX_SPEED):
				moveSpeed = moveSpeed+10

	elif(buttons["pad_down"]==True):
		if(last_buttons==None or last_buttons["pad_down"] == False):
			print "turn decrease"

			if(moveSpeed-10 >= MIN_SPEED):
				moveSpeed = moveSpeed - 10

	elif(buttons["right_shoulder"]==True):
		arm_pos = arm_pos+10
		if(arm_pos > 180):
			arm_pos = 180
		drive("set_probe")
	elif(buttons["left_shoulder"]==True):
		arm_pos = arm_pos-10
		if(arm_pos < 0):
			arm_pos = 0
		drive("set_probe")

	elif(buttons["cross"]==True):
		if(grip_pos+10 <= MAX_GRIP):
			grip_pos = grip_pos=grip_pos+10
		drive("set_probe")
	elif(buttons["square"]==True):
		if(grip_pos-10 >= MIN_GRIP):
			grip_pos = grip_pos - 10
		drive("set_probe")

	elif(buttons["push_right"]==True):
		if(last_buttons==None or last_buttons["push_right"] == False):
			if(turnSpeed+10 <= MAX_SPEED):
				turnSpeed = turnSpeed+10
	elif(buttons["push_left"]==True):
		if(last_buttons==None or last_buttons["push_left"] == False):
			if(turnSpeed-10 >= MIN_SPEED):
				turnSpeed = turnSpeed - 10
	else:
		drive("park")

	return buttons

try:

	last_buttons = None

	while(True):
		last_buttons = read_loop(last_buttons)

		time.sleep(0.025)
except KeyboardInterrupt:
	drive("park")
	drive("quit")


