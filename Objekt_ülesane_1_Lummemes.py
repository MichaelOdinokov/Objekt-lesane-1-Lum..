import pygame
pygame.init()
ekraani_pind=pygame.display.set_mode((640,480))
ekraani_pind.fill((20,234,242))# fill- värvid
pygame.display.set_caption("Lummemes - Michael Odinokov")# set_caption
#ristkülik
ristkülik=pygame.Rect(0,300,640,180)
pygame.draw.rect(ekraani_pind,(30,47,158),ristkülik)

#Lummes, ovaal
ovaal1=pygame.Rect(242,110,80,80)
pygame.draw.ellipse(ekraani_pind,(252,252,252),ovaal1)

ovaal2=pygame.Rect(232,185,100,100)
pygame.draw.ellipse(ekraani_pind,(252,252,252),ovaal2)

ovaal3=pygame.Rect(222,280,120,120)
pygame.draw.ellipse(ekraani_pind,(252,252,252),ovaal3)

ovaal4=pygame.Rect(262,130,10,10)
pygame.draw.ellipse(ekraani_pind,(0,0,0),ovaal4)

ovaal5=pygame.Rect(292,130,10,10)
pygame.draw.ellipse(ekraani_pind,(0,0,0),ovaal5)
#päike


kollane=[255,255,0]
joon=pygame.Rect(20,20,100,100)
pygame.draw.line(ekraani_pind,kollane,(20,20),(100,150),5)

kollane=[255,255,0]
joon=pygame.Rect(20,20,100,100)
pygame.draw.line(ekraani_pind,kollane,(50,50),(200,10),5)

kollane=[255,255,0]
joon=pygame.Rect(20,20,100,100)
pygame.draw.line(ekraani_pind,kollane,(10,10),(10,100),5)



polygon=pygame.Rect(-10,-10,90,90)
pygame.draw.ellipse(ekraani_pind,(255,255,51),polygon)



#joon
orange=[255,144,0]
joon=pygame.Rect(242,0,100,100)
pygame.draw.line(ekraani_pind,orange,(222,150),(285,150),4)


whithe=[255,255,255]
joon=pygame.Rect(232,185,100,100)
pygame.draw.line(ekraani_pind,whithe,(90,210),(285,210),5)

whithe=[255,255,255]
joon=pygame.Rect(232,185,100,100)
pygame.draw.line(ekraani_pind,whithe,(400,210),(285,210),5)

#polygon
polygon=pygame.Rect(252,80,20,40)
pygame.draw.ellipse(ekraani_pind,(252,252,10),polygon)

polygon=pygame.Rect(290,80,20,40)
pygame.draw.ellipse(ekraani_pind,(252,252,10),polygon)


pygame.display.flip()
while True:
    event=pygame.event.poll()# poll - proverjaet sobitija
    if event.type==pygame.QUIT:
        break
pygame.quit()
