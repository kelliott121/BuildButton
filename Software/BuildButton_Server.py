from pyrobot import *
import win32gui
import serial
import time

appMap = {	'Sublime Text 2'	: [Keys.left_control, Keys.b],
			'Visual Studio'		: [Keys.left_control, Keys.left_shift, Keys.b],
			'Motion Composer'	: [Keys.f5]}

robot = Robot()

#arduino = arduinoserial.SerialPort('/dev/ttyUSB0', 9600)
arduino = serial.Serial('COM11', 9600, timeout=0.1)

def buttonLight(OnOff):
	if (OnOff):
		# Light the button
		arduino.write('1')
	else:
		# Unlight the button
		arduino.write('0')

def canWeBuildIt(winName):
	# Check if it is one of the buildable applications
	for key in appMap.keys():
		if key in winName:
			return True
	return False

def getBuildKey(winName):
	for key in appMap.keys():
		if key in winName:
			return key

def sendKeys(keyArray):
	for key in keyArray:
		robot.key_press(key)
	for key in keyArray:
		robot.key_release(key)

while True:
    activeWindowName=win32gui.GetWindowText(win32gui.GetForegroundWindow())

    if canWeBuildIt(activeWindowName):
	   	buttonLight(True)
    else:
        buttonLight(False)

    try:
    	btnText = arduino.readline()
    except arduino.SerialTimeoutException:
    	btnText = ""

    if ('press' in btnText) and canWeBuildIt(activeWindowName):
    	buildKey = getBuildKey(activeWindowName)
    	sendKeys(appMap[buildKey])

    time.sleep(0.1)