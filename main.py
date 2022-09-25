# Programa principal
import sys
import funciones_ejemplo

funciones_ejemplo.tabla_multiplicar(4)

import pygame
import os
os.environ["SDL_VIDEODRIVER"] = "dummy"

pygame.init()

size= (800,500)
screen = pygame.display.set_mode(size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((70,120,200))

    pygame.display.flip()

pygame.display.quit()
