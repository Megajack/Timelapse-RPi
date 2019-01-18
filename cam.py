import picamera
import time
#import datetime
#import sleep

camera = picamera.PiCamera()
#camera = start_preview()
#camera.brightness = 50

#camera.exposure_mode = 'auto'
#camera.resolution = (3280, 2464)
camera.resolution = (1280, 962)
#camera.iso = 800
#camera.shutter_speed = 100000

#camera.resolution = (1024, 768)
#camera.vflip = True
#camera.hflip = True
#date = datetime.now().strftime("%a-%d.%m.%Y-%H:%M:%S")
#num = '/home/pi/Desktop/cam/img-' + date + '.jpg'

for i in range(8000):
    time.sleep(10)
    camera.capture('1/image{0:04d}.jpg'.format(i))
#camera.stop_preview()
