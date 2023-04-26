import pygame
from random import*
import sys

def Päripäeva(posX,posY,sammX,sammY):#По часовой
    if posX==0 and posY==0:
        sammX=1
        sammY=0
    elif posX==X-pilt.get_rect().width and posY==0:
        sammX=0
        sammY=1
    elif posX==X-pilt.get_rect().width and posY==Y-pilt.get_rect().height:
        sammX=-1
        sammY=0
    elif posX==0 and posY==Y-pilt.get_rect().height:
        sammX=0
        sammY=-1
    posX+=sammX
    posY+=sammY
    return posX, posY, sammX, sammY


def Vastupäeva(posX,posY,sammX,sammY):#Против часовой
    if posX==0 and posY==Y-pilt.get_rect().height:
        sammX=1  
        sammY=0
    elif posX==X-pilt.get_rect().width and posY==Y-pilt.get_rect().height:
        sammX=0
        sammY=-1
    elif posX==X-pilt.get_rect().width and posY==0:
        sammX=-1
        sammY=0
    elif posX==0 and posY==0:
        sammX=0
        sammY=1
    posX+=sammX
    posY+=sammY
    return posX, posY, sammX, sammY


def R(posX,posY,sammX,sammY):#оталкивается от кроёв
    posX=random.randint(0,X-pilt.get_rect().width)
    posY=random.randint(0,Y-pilt.get_rect().height)
    if posY<=0 or posY>=Y-pilt.get_rect().height:
        sammY=-sammY
    if posX<=0 or posX>=X-pilt.get_rect().width:
        sammX=-sammX

def YX(posX,posY,sammX,sammY): #вверх ввниз
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
    return posX, posY, sammX, sammY



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


v=[Vastupäeva,Päripäeva,R,YX]
v_list=v

while  not lõpp:
    kell.tick(120)
    events=pygame.event.get()
    for i in pygame.event.get():       
        if i.type==pygame.QUIT:
             lõpp=True
        funktsioon=random.shuffel(v)
        if funktsioon==Päripäeva:
            Päripäeva(posX,posY,sammX,sammY)
        elif funktsioon==Vastupäeva:
            Vastupäeva(posX,posY,sammX,sammY)
        elif funktsioon==Random:
            Random(posX,posY,sammX,sammY)
        elif funktsioon ==YX:
            YX(posX,posY,sammX,sammY)        
    ekraan.blit(pilt,(posX,posY))
    pygame.display.flip()
    ekraan.fill(roheline)
pygame.quit()