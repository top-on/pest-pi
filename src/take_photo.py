""" Take picture with picamera. """

from picamera import PiCamera

camera = PiCamera()
camera.capture('img/test_py.png')
camera.close()
