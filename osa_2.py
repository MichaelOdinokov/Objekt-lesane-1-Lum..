import pygame
import random
import sys

def Maja(x,y,laius,kõrgus,pind,värv):
    point=[(x,y- (3/4.0) * kõrgus), (x,y), (x+laius,y), (x+laius,y-(3/4.0)*kõrgus), (x,y- (3/4.0*kõrgus)), (x+laius/2.0,y-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
    
    pygame.draw.lines(pind,värv,False,point,suurus)

pygame.init()
pind=pygame.display.set_mode((640,480))
pygame.display.set_caption("Maa objektid - Michael Odinokov")# set_caption

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

fon=[r,g,b]
green=[r,g,b]

r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)

majavärv=[r,g,b]



suurus=random.randint(1,10)
pind.fill(fon)

#maa
ristkülik=pygame.Rect(0,400,640,180)
pygame.draw.rect(pind,(10,233,40),ristkülik)

#Uks
uks=pygame.Rect(200,200,100,100)
pygame.draw.rect(pind,(255,0,0),uks)

Maja(100,400,300,400,pind,majavärv)



for i in range(10):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    varv=[r,g,b]
    
    laius=random.randint(1,80)
    kõrgus=random.randint(1,80)

    x=random.randint(0,610-laius)# figura 30 nuzhna sdelati ostup 30 
    y=random.randint(0,450-kõrgus)
    pygame.draw.rect(pind, varv,[x,y,laius,kõrgus])




pygame.display.flip()
while True:
    event=pygame.event.poll()# poll - proverjaet sobitija
    if event.type==pygame.QUIT:
        break
pygame.quit()
