import picamera
import time
import datetime

date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
camera = picamera.PiCamera()
#camera = start_preview()
#camera.brightness = 50

#camera.exposure_mode = 'auto'
camera.resolution = (3280, 2464)
#camera.resolution = (1280, 962)
#camera.iso = 800
#camera.shutter_speed = 100000

#camera.resolution = (1024, 768)
#camera.vflip = True
#camera.hflip = True
#date = datetime.now().strftime("%a-%d.%m.%Y-%H:%M:%S")
#num = '/home/pi/Desktop/cam/img-' + date + '.jpg'
time.sleep(10)
camera.capture('pics-single/' + date + '.jpg')
