X9
==
An application health/status monitor

X9 uses an Arduino

Usage
--------
First you need to export two environment variables:
* ``APPLICATION_ENDPOINT``: The URL that returns a http status code 200 when the application is healthy
* ``ARDUINO_PORT``: The serial port that your Arduino is connected to
* Run it: ``$ python X9.py``



TODO
----
* Write a proper runnable python script
* Refactor everything
* Wirte some tests
* Use native code instead of firmata
* Use KiCad instead of Fritzing
