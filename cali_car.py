import picar
from picar import back_wheels, front_wheels
from enum import Enum

config = "/home/pi/dmcar-student/picar/config"


class State(Enum):
    STRAIGHT = 0
    LEFT = 1
    RIGHT = 2


class CalibratedCar:
    def __init__(self, config='config', lts_offset=0, rts_offset=0):
        picar.setup()

        self.stat = State.STRAIGHT

        self.bw = back_wheels.Back_Wheels(db=config)
        self.fw = front_wheels.Front_Wheels(db=config)

        self.bw.ready()
        self.fw.ready()

        self.lts_offset = lts_offset
        self.rts_offset = rts_offset

    def set_speed(self, speed):
        self.bw.speed = speed

    def st(self):
        self.fw.turn_straight()

        self.cali()
        self.stat = State.STRAIGHT

    def fd(self):
        self.st()

        self.bw.forward()

    def bk(self):
        self.fw.turn_straight()
        self.bw.backward()

        self.cali()
        self.stat = State.STRAIGHT

    def rt(self):
        self.stat = State.RIGHT
        self.fw.turn_right()

    def lt(self):
        self.stat = State.LEFT
        self.fw.turn_left()

    def stop(self):
        self.bw.stop()

    def cali(self):
        if self.stat == State.LEFT:
            self.fw.turn(self.lts_offset)
        elif self.stat == State.RIGHT:
            self.fw.turn(self.rts_offset)
