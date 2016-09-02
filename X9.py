import os
import pyfirmata
import requests
import time

RED = 8
YELLOW = 9
GREEN = 10
BUZZER = 6

port = os.environ.get('ARDUINO_PORT')
application_endpoint = os.environ.get('APPLICATION_ENDPOINT')

arduino = pyfirmata.Arduino(port)

buzzer = arduino.digital[BUZZER]
buzzer.mode = 3
buzzer.write(0.0)

print "ARDUINO_PORT: " + port
print "APPLICATION_ENDPOINT: " + application_endpoint

buzzer.write(1.0)
time.sleep(0.5)
buzzer.write(0.0)

arduino.digital[GREEN].write(1)
time.sleep(2)
arduino.digital[GREEN].write(0)

time.sleep(2)
arduino.digital[YELLOW].write(1)
time.sleep(2)
arduino.digital[YELLOW].write(0)

time.sleep(2)
arduino.digital[RED].write(1)
time.sleep(2)
arduino.digital[RED].write(0)


buzzer.write(1.0)
time.sleep(0.5)
buzzer.write(0.0)


def play_buzzer(delay):
    for i in range(5):
        buzzer.write(1.0)
        time.sleep(delay)
        buzzer.write(0)
        time.sleep(delay)


def alert():
    arduino.digital[GREEN].write(0)
    arduino.digital[YELLOW].write(0)
    arduino.digital[RED].write(1)
    play_buzzer(0.5)


def warning():
    arduino.digital[GREEN].write(0)
    arduino.digital[YELLOW].write(1)
    arduino.digital[RED].write(0)
    play_buzzer(0.1)


def ok():
    buzzer.write(0)
    arduino.digital[GREEN].write(1)
    arduino.digital[YELLOW].write(0)
    arduino.digital[RED].write(0)


def printit():
    try:
        time.sleep(5)
        r = requests.get(application_endpoint,
                         timeout=5.0)
        if r.status_code == 200:
            ok()
            print "ok"
        else:
            alert()
            print "alert"
    except Exception, e:
        print e
        warning()
        print "warning"


while True:
    printit()
