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

pilt=pygame.image.load("pika.png")
pind.blit(pilt,(100, 100))

pilt=pygame.image.load("B.png")
pind.blit(pilt,(500, 20,))

pilt=pygame.image.load("O.png")
pind.blit(pilt,(230, 20))

font=pygame.font.Font(None,25)
tekst=font.render("Hello, Michael!", True, (0,0,0)) 
pind.blit(tekst, (270,40))


pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        break
pygame.quit()