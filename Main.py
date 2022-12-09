#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

import pygame
from pygame.locals import *
import time
import sys

from Scene import Scene
from GamePanel import GamePanel
from MainMenuScene import MainMenuScene
import Constants, Helper
import ValueManager


pygame.init()                                                                   #Initialisation du module pygame


infoMonitor = pygame.display.Info()
Constants.screenWidth = infoMonitor.current_w
Constants.screenHeight = infoMonitor.current_h
screen = pygame.display.set_mode((Constants.screenWidth,Constants.screenHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)#Initialisation de la fenetre

pygame.display.set_caption('PyBall')

print("fenetre size :", (infoMonitor.current_w,infoMonitor.current_h))
pygame.key.set_repeat(1, 10)                                                    #Configuration de la repetition des touches


FPS = int(ValueManager.get("FPS", "30"))                                        #Nombre d'image par seconde
Constants.FPS = FPS

startTime, timeMillis, waitTime, totalTime, frameCount = 0, 0, 0, 0, 0          #Variables pour reglages FPS
targetTime = 1/FPS
running = True

gamePanel = GamePanel(screen, Constants.screenWidth, Constants.screenHeight)      #Le moteur qui permet de changer de Scene

while running:
    startTime = time.time()                                                     #Enregistre le temps au debut de la frame

    for event in pygame.event.get():                                            #Distribue les events au gamePanel
        gamePanel.onEvent(event)


    gamePanel.update()                                                          #Update gamePanel donc la scene en cours d'affichage
    gamePanel.draw()                                                            #Dessine la scene en cours

    timeMillis = (time.time() - startTime)                                      #Compte le temps qui s'est ecoule depuis le debut de la frame

    if timeMillis < targetTime:                                                 #On test si il reste du temps avant la prochaine frame
        waitTime = targetTime - timeMillis                                      #Calcul le temps restant avant la prochaine frame
        time.sleep(waitTime)                                                    #Attend la prochaine frame

    totalTime = totalTime + (time.time() - startTime)                           #Ajoute le temps de la frame aux compteurs de temps de la frame
    frameCount = frameCount + 1                                                 #Incremente le nombre de frame

    if frameCount == FPS:                                                       #Test si le nb de frame == Constants.FPS comme configure
        averageFPS = 1 / (totalTime/frameCount)                                 #Calcul le FPS moyen (Il doit etre le plus proche possible de FPS)
        frameCount = 0                                                          #Reinitialise le compteur de frames
        totalTime = 0                                                           #Reinitialise le temps de 30 frames
        #print("averageFPS :", averageFPS)                                      #Affiche le FPS moyen
        FPS = int(ValueManager.get("FPS", "30"))
        Constants.FPS = FPS
        targetTime = 1/FPS

