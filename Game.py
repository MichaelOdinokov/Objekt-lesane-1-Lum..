import pygame
import random
import sys
from random import*



pygame.init()
X, Y =640, 480
ekraan=pygame.display.set_mode([X, Y])
pygame.display.set_caption("Maa objektid - Michael Odinokov")

# Задаем цвет фона
fon = pygame.image.load("dzungli.png")


# maugli
mau=pygame.image.load("Maugli.png")
posX, posY=X- mau.get_rect().width, Y-mau.get_rect().height
samm=2



# õuna

õuna=pygame.image.load("õuna.png")
posX1, posY1=X- õuna.get_rect().width, Y-õuna.get_rect().height
samm=5
posX1, posY1=0,0

kell=pygame.time.Clock()
gameover=False

while True:
    kell.tick(60)
    events=pygame.event.get()
    for event in events:
        if event.type==pygame.QUIT:
            gameover=True
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        posX -= samm
    if keys[pygame.K_RIGHT]:
        posX += samm
    if keys[pygame.K_UP]:
        posY -= samm
    if keys[pygame.K_DOWN]:
        posY += samm
    ekraan.blit(fon, (0, 0))
    ekraan.blit(mau, (posX, posY))
    ekraan.blit(õuna, (posX, posY))
    pygame.display.flip()
pygame.quit()