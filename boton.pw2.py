from threading import Thread
import time
import pygame_widgets
import pygame
from pygame_widgets.button import Button

FPS = 30
# motor = True
catx = 5
caty = 380
pared = [False, (440, 400, 120, 20)]
colorPared = (0,0,0)
direction = 'up'
angulo = 0
posicion = [5,380]

import clases_pw as cpw

pygame.init()
win = pygame.display.set_mode((600, 600))

tank = cpw.robot(posicion)
def detectar_pared(pared, catx, caty):
    if pared[0]:
        if catx > 450:
            d = pared[1][1]-120 -caty
            if d>0:
                return d, pared
    return 200, pared

def detectar_bordes(tank):
    if tank.motor == False:
        return tank.direccion
    else:
        if tank.direccion == 'right':
            if tank.posicion[0] >= 475:
                tank.direccion = tank.rotar('down')
        elif tank.direccion == 'down':
            if tank.posicion[1] >= 480:
                tank.direccion = tank.rotar('left')
        elif tank.direccion == 'left':
            if tank.posicion[0] <= 5:
                tank.direccion = tank.rotar('up')
        elif tank.direccion == 'up':
            if tank.posicion[1] <= 5:
                tank.direccion = tank.rotar('right')
    return tank.direccion

def boton_click():
    global pared, colorPared #, motor
    if pared[0]:
        colorPared = (0,0,0)
#        motor = True
    else:
        colorPared= (255,255,255)
    pared[0] = not(pared[0])

button2 = Button(win, 200, 200, 108, 60, text='Pared',
               onClick=lambda: boton_click())
fpsClock = pygame.time.Clock()

run = True
solo1 = True
while run:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            run = False
            break
    if run == False:
        break
    win.fill((0,0,0))
    pygame.draw.rect(win, colorPared, pared[1])
    
    tank.encender()
    
    for i in range(10):
        tank.avanzar()
        x = tank.posicion[0]
        y = tank.posicion[1]
        tank.direccion = detectar_bordes(tank)
        win.blit(tank.imagen, (x, y))
        pygame_widgets.update(events)
        pygame.display.update()
        fpsClock.tick(FPS)
    print(tank.posicion)
    
    tank.parar()

    win.blit(tank.imagen, (tank.posicion[0], tank.posicion[1]))
    pygame_widgets.update(events)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()