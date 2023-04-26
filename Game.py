import pygame
import random
import sys

pygame.init()
X, Y = 640, 480
ekraan = pygame.display.set_mode([X, Y])
pygame.display.set_caption("Maa objektid - Michael Odinokov")

# Задаем цвет фона
fon = pygame.image.load("12.png")
ekraan.blit(fon, (0, 0))

# Загружаем картинку
pilt = pygame.image.load("Monkey.png")
posX, posY = X - pilt.get_rect().width, Y - pilt.get_rect().height
sammX, sammY = 0, 0

kell = pygame.time.Clock()
while True:
    kell.tick(60)
    events = pygame.event.get()
    for i in pygame.event.get():       
        if i.type == pygame.QUIT:
            sys.exit()
    ekraan.blit(fon, (0, 0))
    ekraan.blit(pilt, (posX, posY))
    pygame.display.flip()
pygame.quit()
