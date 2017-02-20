import sys

from pmotor import wildserial

rover = wildserial('USB0')

quit=False
turnTime=0.5
moveSpeed=850
moveTime=0.5
while(quit==False):
	sys.stdout.write( "Command: ")
	line=raw_input()
	if(line=='q'):
		quit=True
		rover.quit()
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

	elif(line=="]"):
		if(moveSpeed+100<2000):
			moveSpeed+=100
			print "Move: "+str(moveSpeed)
		else:
			print "Speed must not exceed 1900"
	elif(line=="["):
		moveSpeed-=100
		print "Move: "+str(moveSpeed)
