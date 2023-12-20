FPS = 30
motor = True
catx = 5
caty = 380
pared = [False, (440, 400, 120, 20)]
colorPared = (0,0,0)
direction = 'up'
angulo = 0

from funciones_pw import *

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

def boton_click():
    global motor, pared, colorPared
    if pared[0]:
        colorPared = (0,0,0)
        motor = True
    else:
        colorPared= (255,255,255)
    pared[0] = not(pared[0])

catImg = pygame.image.load('Imagenes/tank_sprite2.jpeg')
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
    catx, caty = avanzar(direction, motor, catx, caty)
    
    direction, angulo = detectar_bordes(direction, motor, catx, caty, angulo)
    catImg2 = pygame.transform.rotate(catImg, angulo)
    distancia, pared = detectar_pared(pared, catx, caty)
    if distancia < 20 and motor == True:
        motor= parar()

    win.blit(catImg2, (catx, caty))
    pygame_widgets.update(events)
    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
