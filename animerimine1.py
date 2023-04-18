import pygame
import random
import sys

pygame.init()
pind=pygame.display.set_mode((640,480))

kollane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]

#ekraani suurus
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])
pygame.display.set_caption("Maa objektid - Michael Odinokov")# set_caption
ekraan.fill(roheline)
kell=pygame.time.Clock()
pilt=pygame.image.load("snoopy.png")
posX=X-78
posY=Y-100
lõpp=False
samm=2
while not lõpp:
    kell.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT():
            sys.exit()
    ekraan.blit(pilt,(posX,posY))
    posX-=samm
    pygame.display.flip()
pygame.quit()


