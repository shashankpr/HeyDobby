from matrixio_hal import everloop
from collections import deque
import time


def set_everloop_detection():
    image = everloop.Image(init_color_name='green')
    image.render()

def set_everloop_listening():
    # LED rotation
    image = everloop.Image()
    image.leds[0].red = 20
    cnt = 1
    for i in range(1, len(image.leds)):
        if i <= everloop.EVERLOOP_SIZE // 2:
            image.leds[i].red = 17
            image.leds[i].blue = cnt // 5
            cnt += 1
        else:
            image.leds[i].red = 17
            image.leds[i].green = cnt // 5
            cnt -= 1
    return image

def set_everloop_response():
    image = everloop.Image(init_color_name='blue')
    image.render()

def set_everloop_error():
    image = everloop.Image(init_color_name='red')
    image.render()
