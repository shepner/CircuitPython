import board
from digitalio import DigitalInOut, Direction, Pull
import adafruit_dotstar as dotstar
import time

duration=1*60 #this is how long we are going to wait between cycles

# Digital input on D0
d0 = DigitalInOut(board.D0)
d0.direction = Direction.INPUT
d0.pull = Pull.DOWN

# Digital input on D1
d1 = DigitalInOut(board.D1)
d1.direction = Direction.INPUT
d1.pull = Pull.DOWN

# Digital output on D2
d2 = DigitalInOut(board.D2)
d2.direction = Direction.OUTPUT
#d2.pull = Pull.UP


#internal attached dotstar led
dot = dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1, brightness=0.2)
dot[0] = [0, 0, 0]

state=False
while True:

    if d0.value:
        state=True
        dot[0] = [255, 0, 0]
        time.sleep(10)

    if d1.value:
        state=True
        dot[0] = [0, 255, 0]
        time.sleep(10)

    if state:
        state=False
        dot[0] = [255, 255, 255]
        time.sleep(duration)
    else:
        dot[0] = [10, 10, 10]



