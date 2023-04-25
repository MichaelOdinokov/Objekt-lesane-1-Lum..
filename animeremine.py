import pygame
from random import*
import sys

def K(posX,posY,sammX,sammY):#По часовой стрелке
    if posX==0 and posY==0:
        sammX=1
        sammY=0
    if posX==X-pilt.get_rect().width and posY==0:
        sammX=0
        sammY=1
    if posX==X-pilt.get_rect().width and posY==Y-pilt.get_rect().height:
        sammX=-1
        sammY=0
    if posX==0 and posY==Y-pilt.get_rect().height:
        sammX=0
        sammY=-1
    posX+=sammX
    posY+=sammY

def K180(posX,posY,sammX,sammY):#против часовой
    if posX==0 and posY==Y-pilt.get_rect().height:
        sammX=1  
        sammY=0
    if posX==X-pilt.get_rect().width and posY==Y-pilt.get_rect().height:
        sammX=0
        sammY=-1
    if posX==X-pilt.get_rect().width and posY==0:
        sammX=-1
        sammY=0
    if posX==0 and posY==0:
        sammX=0
        sammY=1
    posX+=sammX
    posY+=sammY

def R(posX,posY,sammX,sammY):#оталкивается от кроёв
    posX=random.randint(0,X-pilt.get_rect().width)
    posY=random.randint(0,Y-pilt.get_rect().height)
    if posY<=0 or posY>=Y-pilt.get_rect().height:
        sammY=-sammY
    if posX<=0 or posX>=X-pilt.get_rect().width:
        sammX=-sammX

def YX(posX,posY,sammX,sammY):
    if posX<=0:
        sammX=1
    if posY<=0:
        sammY=1
    if posX>=X-pilt.get_rect().width:
        sammX=-1
    if posY>=Y-pilt.get_rect().height:
        sammY=-1
    posX+=sammX
    posY+=sammY

lõpp=False
sammX=2
sammY=0
pygame.init()
pind=pygame.display.set_mode((640,480))
#ekraani suurus
X=640
Y=480
ekraan=pygame.display.set_mode([X,Y])

pygame.display.set_caption("Maa objektid - Michael Odinokov")# set_caption
kollane=[255,255,10]
punane=[255,0,0]
hall=[200,200,200]
roosa=[255,150,255]
roheline=[100,255,100]
ekraan.fill(roheline)
kell=pygame.time.Clock()
pilt=pygame.image.load("pika2.png")

posX=X-pilt.get_rect().width 
posY=Y-pilt.get_rect().height

posX1=X+pilt.get_rect().width
posY1=Y+pilt.get_rect().height

v=[K,K180,R,YX]
v_list=v

while  not lõpp:
    kell.tick(120)
    events=pygame.event.get()
    for i in pygame.event.get():       
        if i.type==pygame.QUIT:
            random.choice(v)
        exit.sys()
    ekraan.blit(pilt,(posX,posY))
    pygame.display.flip()
    ekraan.fill(roheline)
pygame.quit()
