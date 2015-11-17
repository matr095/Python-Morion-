#Morpion fait par MatR (Mathieu Rossetto)
#Disponible sur mathieu-rossetto.com
#Copyright 2015 - MatR

__author__ = 'mathieurossetto'

import pygame
from pygame import mixer
pygame.init()
pygame.mixer.init()


fenetre = pygame.display.set_mode((800,600))
pygame.display.set_caption("Morpion by MatR")
fond = pygame.draw.rect(fenetre, (25,25,25), (0,0,800,600))
pygame.display.flip()


def jeu():

    a = 100
    while (a <=300):
        global maVar
        maVar = "carre" + str(a)
        print(maVar)
        maVar = pygame.draw.rect(fenetre, (150,150,150), (a,100,90,90))
        a+=100
    pygame.display.flip()


    b = 100
    while (b <=300):
        global maVar1
        maVar1 = "carre1" + str(b)
        print(maVar1)
        maVar1 = pygame.draw.rect(fenetre, (150,150,150), (b,200,90,90))
        b+=100
    pygame.display.flip()

    c = 100
    while (c <=300):
        global maVar2
        maVar2 = "carre2" + str(c)
        print(maVar2)
        maVar2 = pygame.draw.rect(fenetre, (150,150,150), (c,300,90,90))
        c+=100
    pygame.display.flip()

    font = pygame.font.Font(None, 25)
    text2 = font.render("Joueur orange = Clic gauche", 1, (250, 250, 210))
    fenetre.blit(text2, (100,401))
    text3 = font.render("Joueur bleu = Clic droit", 1, (250, 250, 210))
    fenetre.blit(text3, (100,421))

    font = pygame.font.Font(None, 36)
    text2 = font.render("Morpion par MatR", 1, (250, 250, 210))
    fenetre.blit(text2, (100,5))
    pygame.display.flip()


    text0 = font.render("Recommencer", 1, (250, 250, 210))
    fenetre.blit(text0, (100,531))
    pygame.display.flip()

    continuer = 1
    while (continuer):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continuer = 0

            poss = pygame.mouse.get_pos()



            if (100 <= poss[0] <= 200 and 100 <= poss[1] <= 200):
                 if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                               print(poss[0])
                               orange = pygame.draw.circle(fenetre, (255,100,0), (150,150), 45,45)
                               pygame.display.flip()
                               break
                 if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                               print(poss[0])
                               bleu = pygame.draw.circle(fenetre, (100,100,255), (150,150), 45,45)
                               pygame.display.flip()
                               break


            if (100 <= poss[0] <= 200 and 200 <= poss[1] <= 300):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                       print(poss[0])
                       orange = pygame.draw.circle(fenetre, (255,100,0), (150,250), 45,45)
                       pygame.display.flip()
                       break
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                       print(poss[0])
                       bleu = pygame.draw.circle(fenetre, (100,100,255), (150,250), 45,45)
                       pygame.display.flip()
                       break


            if (100 <= poss[0] <= 200 and 300 <= poss[1] <= 400):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                       print(poss[0])
                       orange = pygame.draw.circle(fenetre, (255,100,0), (150,350), 45,45)
                       pygame.display.flip()
                       break
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                       print(poss[0])
                       bleu = pygame.draw.circle(fenetre, (100,100,255), (150,350), 45,45)
                       pygame.display.flip()
                       break

              #separation

            if (200 <= poss[0] <= 300 and 100 <= poss[1] <= 200):
                 if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                               print(poss[0])
                               orange = pygame.draw.circle(fenetre, (255,100,0), (250,150), 45,45)
                               pygame.display.flip()
                               break
                 if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                               print(poss[0])
                               bleu = pygame.draw.circle(fenetre, (100,100,255), (250,150), 45,45)
                               pygame.display.flip()
                               break


            if (200 <= poss[0] <= 300 and 200 <= poss[1] <= 300):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                       print(poss[0])
                       orange = pygame.draw.circle(fenetre, (255,100,0), (250,250), 45,45)
                       pygame.display.flip()
                       break
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                       print(poss[0])
                       bleu = pygame.draw.circle(fenetre, (100,100,255), (250,250), 45,45)
                       pygame.display.flip()
                       break


            if (200 <= poss[0] <= 300 and 300 <= poss[1] <= 400):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                       print(poss[0])
                       orange = pygame.draw.circle(fenetre, (255,100,0), (250,350), 45,45)
                       pygame.display.flip()
                       break
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                       print(poss[0])
                       bleu = pygame.draw.circle(fenetre, (100,100,255), (250,350), 45,45)
                       pygame.display.flip()
                       break


            #separation

            if (300 <= poss[0] <= 400 and 100 <= poss[1] <= 200):
                 if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                               print(poss[0])
                               orange = pygame.draw.circle(fenetre, (255,100,0), (350,150), 45,45)
                               pygame.display.flip()
                               break
                 if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                               print(poss[0])
                               bleu = pygame.draw.circle(fenetre, (100,100,255), (350,150), 45,45)
                               pygame.display.flip()
                               break


            if (300 <= poss[0] <= 400 and 200 <= poss[1] <= 300):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                       print(poss[0])
                       orange = pygame.draw.circle(fenetre, (255,100,0), (350,250), 45,45)
                       pygame.display.flip()
                       break
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                       print(poss[0])
                       bleu = pygame.draw.circle(fenetre, (100,100,255), (350,250), 45,45)
                       pygame.display.flip()
                       break


            if (300 <= poss[0] <= 400 and 300 <= poss[1] <= 400):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                       print(poss[0])
                       orange = pygame.draw.circle(fenetre, (255,100,0), (350,350), 45,45)
                       pygame.display.flip()
                       break
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 3):
                       print(poss[0])
                       bleu = pygame.draw.circle(fenetre, (100,100,255), (350,350), 45,45)
                       pygame.display.flip()
                       break

            #separation

            if (100 <= poss[0] <= 351 and 531 <= poss[1] <= 541):
                if (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                       fond = pygame.draw.rect(fenetre, (25,25,25), (0,0,800,600))
                       jeu()
                       pygame.display.flip()
                       break







jeu()