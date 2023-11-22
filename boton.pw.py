FPS = 30
motor = True
catx = 5
caty = 380
pared = [False, (440, 400, 120, 20)]
colorPared = (0,0,0)
direction = 'up'

from funciones_pw import *

pygame.init()
win = pygame.display.set_mode((600, 600))
catImg = pygame.image.load('/home/drancope/Imágenes/tank_sprite2.jpeg')
#button = Button(win, 10, 400, 118, 100, image=catImg, onClick=lambda: boton_click())
button2 = Button(win, 200, 200, 108, 60, text='Pared',
               onClick=lambda: boton_click())
fpsClock = pygame.time.Clock()

print("Iniciando bucle")
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
    catx, caty = avanzar(direction, motor, catx, caty)
    if solo1:
        solo1 = False
        print("Avance iniciado, direccion ", direction)
    catImg, catx, caty, direction = detectar_bordes(direction, motor, catx, caty, catImg)
    distancia = detectar_pared(pared, catx, caty)
    if distancia < 20 and motor == True:
        parar()

    win.blit(catImg, (catx, caty))
    pygame_widgets.update(events)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()