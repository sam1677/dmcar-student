'''
**********************************************************************
* Filename    : test-control.py
* Description : test control for servo
* Update      : Lee    2019-02-09    New release
**********************************************************************
'''
from picar import back_wheels, front_wheels
import picar
import time
from cali_car import CalibratedCar


db_file = "/home/pi/dmcar-student/picar/config"

car =  CalibratedCar(
    config = db_file, rts_offset = -10
)

SPEED = 50
while True:
    key = input("> ")

    if key == 'q':
        break

    elif key == 'w':
        car.fd()
        car.set_speed(SPEED)

    elif key == 'x':
        car.bk()
        car.set_speed(SPEED)

    elif key == 'a':
        car.lt()

    elif key == 'd':
        car.rt()

    elif key == 's':
        car.st()

    elif key == 'z':
        car.stop()

    elif key == 'u':
        SPEED += 10
