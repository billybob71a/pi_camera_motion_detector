from picamera import PiCamera
from time import sleep
import datetime

class TakePhoto:
    """ for fileprefixval it will be used like fileprefix-datetime.jgp"""
    def __init__(self, sleepval, locationval, fileprefixval):
        self.sleepval = sleepval
        self.locationval = locationval
        self.fileprefixval = fileprefixval
        self.camera = PiCamera()
    
    def snapshot(self):
        self.camera.start_preview()
        sleep(self.sleepval)
        date = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
        self.camera.capture(self.locationval + '/' + self.fileprefixval + '-' + date + '.jpg') 
        self.camera.stop_preview()
