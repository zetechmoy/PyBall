#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	09/12/2022
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


class PyBall(object):

    def __init__(self, onEvent=None, fullscreen=False):
        pygame.init()                                                                   #Initialisation du module pygame

        if fullscreen:
            infoMonitor = pygame.display.Info()
            Constants.screenWidth = infoMonitor.current_w
            Constants.screenHeight = infoMonitor.current_h

        self.screen = pygame.display.set_mode((Constants.screenWidth,Constants.screenHeight), pygame.HWSURFACE|pygame.DOUBLEBUF)#Initialisation de la fenetre

        pygame.display.set_caption('PyBall')
        pygame.key.set_repeat(1, 10)                                                    #Configuration de la repetition des touches

        self.FPS = int(ValueManager.get("FPS", "30"))                                        #Nombre d'image par seconde
        Constants.FPS = self.FPS

        self.startTime, self.timeMillis, self.waitTime, self.totalTime, self.frameCount = 0, 0, 0, 0, 0          #Variables pour reglages FPS
        self.targetTime = 1/self.FPS

        self.gamePanel = GamePanel(self.screen, Constants.screenWidth, Constants.screenHeight)      #Le moteur qui permet de changer de Scene
        self.onEvent = onEvent
        self.plugins = list()

    def start(self):
        self.running = True
        self.run()

    def stop(self):
        self.running = False

    def addPlugin(self, plugin):
        self.plugins.append(plugin)

    def run(self):
        while self.running:
            self.startTime = time.time()                                                     #Enregistre le temps au debut de la frame

            for event in pygame.event.get():                                            #Distribue les events au gamePanel
                self.gamePanel.onEvent(event)
                if self.onEvent is not None:
                    self.onEvent(event)

                if event.type == Constants.END_EVENT:
                    self.gamePanel.resetPlugins()
                
                if event.type == Constants.START_EVENT:
                    for plugin in self.plugins:
                        self.gamePanel.addPlugin(plugin)

            self.gamePanel.update()                                                          #Update gamePanel donc la scene en cours d'affichage
            self.gamePanel.draw()                                                            #Dessine la scene en cours

            self.timeMillis = (time.time() - self.startTime)                                      #Compte le temps qui s'est ecoule depuis le debut de la frame

            if self.timeMillis < self.targetTime:                                                 #On test si il reste du temps avant la prochaine frame
                self.waitTime = self.targetTime - self.timeMillis                                      #Calcul le temps restant avant la prochaine frame
                time.sleep(self.waitTime)                                                    #Attend la prochaine frame

            self.totalTime = self.totalTime + (time.time() - self.startTime)                           #Ajoute le temps de la frame aux compteurs de temps de la frame
            self.frameCount = self.frameCount + 1                                                 #Incremente le nombre de frame

            if self.frameCount == self.FPS:                                                       #Test si le nb de frame == Constants.FPS comme configure
                # averageFPS = 1 / (totalTime/frameCount)                               #Calcul le FPS moyen (Il doit etre le plus proche possible de FPS)
                self.frameCount = 0                                                          #Reinitialise le compteur de frames
                self.totalTime = 0                                                           #Reinitialise le temps de 30 frames
                #print("averageFPS :", averageFPS)                                      #Affiche le FPS moyen
                self.FPS = int(ValueManager.get("FPS", "30"))
                Constants.FPS = self.FPS
                self.targetTime = 1/self.FPS

