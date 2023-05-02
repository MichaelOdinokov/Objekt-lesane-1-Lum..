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
if posY <= 0:
    sammY = 2
elif posY >= ekraan.get_height() - mau.get_height():
    sammY = -2
posY += sammY
ekraan.blit(mau, (posX, posY))
pygame.display.flip()
pygame.time.delay(10)

# õuna
õuna=pygame.image.load("õuna.png")
posX1, posY1=X-õuna.get_rect().width, Y-õuna.get_rect().height
samm=5
posX1, posY1=10,10
if posY <= 0:
    sammY = 2
elif posY >= ekraan.get_height() - õuna.get_height():
    sammY = -2

# Koldõuna
kõuna=pygame.image.load("kõuna.png")
posX2, posY2=X-õuna.get_rect().width, Y-kõuna.get_rect().height
samm=5
posX1, posY1=5,5
if posY <= 0:
    sammY = 2
elif posY >= ekraan.get_height() - kõuna.get_height():
    sammY = -2



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
    elif keys[pygame.K_RIGHT]:
        posX += samm
    elif keys[pygame.K_UP]:
        posY -= samm
    elif keys[pygame.K_DOWN]:
        posY += samm
    
   
    ekraan.blit(mau, (posX, posY))
    ekraan.blit(õuna, (posX1, posY1))
    ekraan.blit(kõuna, (posX2, posY2))
    pygame.display.flip()
    pygame.time.delay(10)
    ekraan.blit(fon, (0, 0))
pygame.quit()