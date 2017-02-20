import sys
import time

from fake import wildserial

rover = wildserial('USB0')
rover.setup()

time.sleep(1.5)
print "set up done. OK"
quit=False
turnTime=0.5
moveSpeed=850
moveTime=0.5

def drive(line):
	global moveTime
	print( "Command: " + line)

	if(line=='q'):
		quit=True
		rover.quit()
	elif(line=='p'):
		rover.stop()
	elif(line=='w'):
		rover.go('forwards', moveSpeed,moveTime)
	elif(line=='s'):
		rover.go('reverse', moveSpeed, moveTime)
	elif(line=='a'):
		rover.go('left', 1000, turnTime)
	elif(line=='d'):
		rover.go('right', 1000, turnTime)
	elif(line=="1"):
		moveTime-=0.5
		print "Move time: "+str(moveTime) +" seconds"
	elif(line=="2"):
		moveTime+=0.5
		print "Move time: "+str(moveTime) +" seconds"

moveTime=0.5
print "forwards started"
#drive('w')
#time.sleep(moveTime)
#print "stop"
#drive('p')
#time.sleep(moveTime)
#drive('q')

from joystick import ps3
ps = ps3(0)
ps.connect()

def read_loop():
	ps.pump()
	buttons = ps.get_buttons()
	if(buttons["square"]==True):
		drive('w')
	elif(buttons["cross"]==True):
		drive('s')
	else:
		drive('p')
	#print buttons
	print str(1)
try:
	while(True):
		read_loop()
		time.sleep(0.025)
except KeyboardInterrupt:
	drive('p')
	drive('q')


