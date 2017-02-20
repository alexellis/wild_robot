wild_robot
===========

> Drive a Wild Thumper robot with a PS3 controller or keyboard.

This repository accompanies a blog post: http://blog.alexellis.io/piwars-v2-0/

The state of this repository will start as a code-dump and will be gradually documented as time permits. 

### Initial documentation:

#### Pre-reqs
* sixpair must be downloaded and installed
* Genuine PS3 controller is needed
* Arduino nano or similar programmed and attached to /dev/tty*
* Pygame is a depdency for reading the game controller

#### Operating the robot

The entrypoint and main control-loop is in [drive.py](https://github.com/alexellis/wild_robot/blob/master/drive.py).

* Controller button/axis presses are picked up from PyGame via [joystick.py](https://github.com/alexellis/wild_robot/blob/master/joystick.py)
* Motor/servo commands are sent to an Arduino via [arduino.py](https://github.com/alexellis/wild_robot/blob/master/arduino.py)


#### Controls:
 
* `[select]` button will safely shut-down the robot if you hold it in.
* `[left_trigger]/[right_trigger]` moves forwards/backwards

You can also drive the robot with rudimentary controls without a PS3 controller if you use [keyboard_drive.py](https://github.com/alexellis/wild_robot/blob/master/keyboard_drive.py).

### Todo:

```
[x] Scrape Python code from robot
[ ] Re-test python code after being mothballed
[ ] Link back to blog post
[ ] Find / reconstitute Arduino motor-controller code in C
```
