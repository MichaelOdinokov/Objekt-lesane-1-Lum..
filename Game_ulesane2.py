import pygame
import random
import sys

pygame.init()
pind=pygame.display.set_mode((640,480))
pind.fill((20,234,242))# fill- värvid
pygame.display.set_caption("Game - Michael Odinokov")# set_caption




ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(pind,(102,0,0),ristkülik)

ristkülik=pygame.Rect(0,200,640,150)
pygame.draw.rect(pind,(128,128,128),ristkülik)
pygame.image.load("12.png")


pygame.display.flip()
while True:
    event=pygame.event.poll()# poll - proverjaet sobitija
    if event.type==pygame.QUIT:
        break
pygame.quit()
