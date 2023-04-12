import pygame
import random
import sys




"""
ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(pind,(102,0,0),ristkülik)

ristkülik=pygame.Rect(0,200,640,150)
pygame.draw.rect(ekraani_pind,(128,128,128),ristkülik)

polygon=pygame.Rect(290,80,20,40)
pygame.draw.ellipse(ekraani_pind,(154,252,10),polygon)
"""
pygame.display.flip()
while True:
    event=pygame.event.poll()# poll - proverjaet sobitija
    if event.type==pygame.QUIT:
        break
pygame.quit()