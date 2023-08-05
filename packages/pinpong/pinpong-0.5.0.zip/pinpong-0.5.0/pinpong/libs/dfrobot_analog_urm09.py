import time
from pinpong.board import gboard,Pin,ADC


class ANALOG_URM09():
    def __init__(self, board = None, pin_obj = None):
        if isinstance(board, Pin):
            pin_obj = board
            board = gboard
        elif board is None:
            board = gboard
        self.board = board
        self.pin_obj = pin_obj
        self.adc0 = ADC(self.pin_obj)

    def distance_cm(self):
        return int(self.adc0.read()*520/1023)

