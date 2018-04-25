from matrixio_hal import everloop
from collections import deque
import time

def set_leds():
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

def rotate_leds(start_rotation=True):
    while start_rotation:
        image = set_leds()
        image.render()
        image.rotate(1)
        time.sleep(0.03)

if __name__ == '__main__':
    rotate_leds()