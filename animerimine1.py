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

posX=X-pilt.get_rect().width
posY=Y-pilt.get_rect().height

posX1=X+pilt.get_rect().width
posY1=Y+pilt.get_rect().height


lõpp=False
sammX=2
sammY=0
while not lõpp:
    kell.tick(60)
    events=pygame.event.get()
    for i in pygame.event.get():
        if i.type==pygame.QUIT():
            sys.exit()
    ekraan.blit(pilt,(posX,posY))

    if posX>X-pilt.get_rect().width or posX<0:        
        sammX=-sammX
    if posY>Y-pilt.get_rect().width or posY<170:
        sammY=-sammY
    if posX<0:
        sammY=2
        sammX=0
        posY=sammY


    posX-=sammX
    posY-=sammY
    
        
            
    pygame.display.flip()
    ekraan.fill(roheline)
pygame.quit()


