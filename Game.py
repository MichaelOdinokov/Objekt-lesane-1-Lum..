import pygame
import random
import sys

pygame.init()
X, Y =640, 480
ekraan=pygame.display.set_mode([X, Y])
pygame.display.set_caption("Maa objektid - Michael Odinokov")

# Задаем цвет фона
fon = pygame.image.load("mere.png")
ekraan.blit(fon, (0, 0))

# shark
shark=pygame.image.load("shark.png")
posX, posY=X- shark.get_rect().width, Y-shark.get_rect().height
samm=2

# kala
kala=pygame.image.load("kala.png")
posX, posY=X- kala.get_rect().width, Y-kala.get_rect().height
samm=10

kell=pygame.time.Clock()
while True:
    kell.tick(60)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            sys.exit()

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
    ekraan.blit(shark, (posX, posY))
    ekraan.blit(kala, (posX, posY))
    pygame.display.flip()
pygame.quit()
