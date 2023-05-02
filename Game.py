import pygame
import random
import sys
import time
import datetime

pygame.init()

X, Y = 640, 480
screen = pygame.display.set_mode([X, Y])
pygame.display.set_caption("Maa objektid - Michael Odinokov")

#Laadi alla pildid
fon= pygame.image.load("dzungli.png")
mau= pygame.image.load("Maugli.png")
õuna= pygame.image.load("õuna.png")
kõuna= pygame.image.load("kõuna.png")

#Kell
kell = pygame.time.Clock()

gameover = False
start_kell = time.time()

# Objektid
mau_pos= [X - mau.get_rect().width, Y - mau.get_rect().height]
mau_speed= 3
#õuna
õuna_pos= [random.randint(0, X - õuna.get_rect().width), 0]
õuna_speed= 2

#kõuna
kõuna_pos= [random.randint(0, X - kõuna.get_rect().width), 0]
kõuna_speed= 10
Muutaja= 0

nimi=input("Nimi:")

while not gameover:
    kell.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    if time.time() - start_kell >= 20:
        with open("results.txt", "a") as f:
            f.write(f"Player: {nimi}\n")
            f.write(f"Date: {datetime.datetime.now()}\n")
            f.write(f"Play time: {time.time() - start_kell} seconds\n")
            f.write(f"Score: {Muutaja}\n")
            f.write("\n")
        print("Время вышло! Результаты сохранены в файл.")
        gameover = True
    # Mau_move
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        mau_pos[0] -= mau_speed
    elif keys[pygame.K_RIGHT]:
        mau_pos[0] += mau_speed
    elif keys[pygame.K_UP]:
        mau_pos[1] -= mau_speed
    elif keys[pygame.K_DOWN]:
        mau_pos[1] += mau_speed

    # kirrus, positsion
    õuna_pos[1] += õuna_speed
    if õuna_pos[1] > Y:
        õuna_pos = [random.randint(0, X - õuna.get_rect().width), 0]

    kõuna_pos[1] += kõuna_speed
    if kõuna_pos[1] > Y:
        kõuna_pos = [random.randint(0, X - kõuna.get_rect().width), 0]

    if pygame.Rect(*mau_pos, *mau.get_size()).colliderect(pygame.Rect(*õuna_pos, *õuna.get_size())):
        Muutaja+= 1
        õuna_pos = [random.randint(0, X - õuna.get_rect().width), 0]

    if pygame.Rect(*mau_pos, *mau.get_size()).colliderect(pygame.Rect(*kõuna_pos, *kõuna.get_size())):
        Muutaja+= 5
        kõuna_pos = [random.randint(0, X - kõuna.get_rect().width), 0]

    screen.blit(fon, (0, 0))
    screen.blit(mau, mau_pos)
    screen.blit(õuna, õuna_pos)
    screen.blit(kõuna, kõuna_pos)
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: " + str(Muutaja), True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
pygame.quit() 
