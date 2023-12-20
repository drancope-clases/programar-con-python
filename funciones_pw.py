from threading import Thread
import time
import pygame_widgets
import pygame
from pygame_widgets.button import Button


def detectar_pared(pared, catx, caty):
    if pared[0]:
        if catx > 450:
            d = pared[1][1]-120 -caty
            if d>0:
                return d, pared
    return 200, pared

def detectar_bordes(direction, motor, catx, caty, angulo):
    if motor == False:
        return direction, angulo

    if direction == 'right':
        if catx >= 475:
            direction = 'down'
            angulo = 180
    elif direction == 'down':
        if caty >= 480:
            direction = 'left'
            angulo = 90
    elif direction == 'left':
        if catx <= 5:
            direction = 'up'
            angulo = 0
    else:
        if caty <= 5:
            direction = 'right'
            angulo = 270
    return direction, angulo

def avanzar(direction, motor, catx, caty):
    if motor:
        if direction == 'right':
            catx += 5
        elif direction == 'down':
            caty += 5
        elif direction == 'left':
            catx -= 5
        elif direction == 'up':
            caty -= 5
    return catx, caty

def parar():
    return False


