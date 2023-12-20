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
    imagen = pygame.image.load('/home/drancope/Imágenes/tank_sprite2.jpeg')
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
        self.imagen = pygame.transform.rotate(self.imagen, direccion)
        self.direccion = direccion
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
            return [10, 10]
        print(self.motor, self.direccion, self.posicion)
        return [0,0]
    def actualizar():
        avanzar()
    def parar(self):
        self.motor = False


