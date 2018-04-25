from matrixio_hal import everloop
from collections import deque
import time

def set_leds():
    image = everloop.Image()
    image.leds[0].blue = 20
    cnt = 1
    for i in range(1, len(image.leds)):
        if i <= everloop.EVERLOOP_SIZE // 2:
            image.leds[i].blue = 17
            image.leds[i].red = cnt // 5
            cnt += 1
        else:
            image.leds[i].blue = 17
            image.leds[i].green = cnt // 5
            cnt -= 1
    image.render()
    image.rotate(1)
    time.sleep(0.03)
