from threading import Thread
import time
import pygame_widgets
import pygame
from pygame_widgets.button import Button


def boton_click():
    global motor, colorPared
    if pared[0]:
        colorPared = (0,0,0)
        motor = True
    else:
        colorPared= (255,255,255)
    pared[0] = not(pared[0])

def detectar_pared(pared, catx, caty):
    if pared[0]:
        if catx > 450:
            d = pared[1][1]-120 -caty
            if d>0:
                return d
    return 200

def detectar_bordes(direction, motor, catx, caty, catImg):

    if motor == False:
        return direction

    if direction == 'right':
        if catx >= 475:
            direction = 'down'
            catImg = pygame.transform.rotate(catImg, 270)
    elif direction == 'down':
        if caty >= 480:
            direction = 'left'
            catImg = pygame.transform.rotate(catImg, 270)
    elif direction == 'left':
        if catx <= 5:
            direction = 'up'
            catImg = pygame.transform.rotate(catImg, 270)
    elif direction == 'up':
        if caty <= 5:
            catImg = pygame.transform.rotate(catImg, 270)
            direction = 'right'
    return catImg, catx, caty, direction

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
    global motor
    motor = False

