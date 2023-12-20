from threading import Thread
import time
import pygame_widgets
import pygame
from pygame_widgets.button import Button

FPS = 30
motor = True
catx = 5
caty = 380
pared = [False, (440, 400, 120, 20)]
colorPared = (0,0,0)
direction = 'up'
angulo = 0
posicion = [5,380]

import clases_pw as cpw

def boton_click():
    global motor, pared, colorPared
    if pared[0]:
        colorPared = (0,0,0)
        motor = True
    else:
        colorPared= (255,255,255)
    pared[0] = not(pared[0])

pygame.init()
win = pygame.display.set_mode((600, 600))

tank = cpw.robot(posicion)

def boton_click():
    global motor, pared, colorPared
    if pared[0]:
        colorPared = (0,0,0)
        motor = True
    else:
        colorPared= (255,255,255)
    pared[0] = not(pared[0])


#button = Button(win, 10, 400, 118, 100, image=catImg, onClick=lambda: boton_click())
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