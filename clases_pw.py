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

class robot:
    motor = False
    posicion = [0,0]
    imagen = pygame.image.load('Imagenes/tank_sprite2.jpeg')
    direccion = 'up'
    def __init__(self, pos):
        self.posicion = pos
    def posActualizar(self, x, y):
        self.posicion[0] = self.posicion[0] + x
        self.posicion[1] = self.posicion[1] + y
    def posSituar(self, x, y):
        self.posicion[0] =  x
        self.posicion[1] =  y
    def rotar(self, direccion):
        angulo = 0
        angulo2 = 0
        if self.direccion == 'up':
            angulo = 0
        elif self.direccion == 'right':
            angulo = 270
        elif self.direccion == 'down':
            angulo = 180
        elif self.direccion == 'left':
            angulo = 90
        if direccion == 'up':
            angulo2 = 0
        elif direccion == 'right':
            angulo2 = 270
        elif direccion == 'down':
            angulo2 = 180
        elif direccion == 'left':
            angulo2 = 90
        angulo = angulo2 - angulo
        self.imagen = pygame.transform.rotate(self.imagen, angulo)
        self.direccion = direccion
        return self.direccion

    def encender(self):
        self.motor = True
    def avanzar(self):
        if self.motor:
            if self.direccion == 'right':
                self.posicion[0] += 5
            elif self.direccion == 'down':
                self.posicion[1] += 5
            elif self.direccion == 'left':
                self.posicion[0] -= 5
            elif self.direccion == 'up':
                self.posicion[1] -= 5
            return [self.direccion, self.posicion]
        #print(self.motor, self.direccion, self.posicion)
        return [0,0]
    def actualizar():
        avanzar()
    def parar(self):
        self.motor = False


