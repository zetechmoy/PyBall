#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------
import pygame

from MainMenuScene import MainMenuScene
from GameScene import GameScene

class GamePanel():

    def __init__(self, scr, sWidth, sHeight):
        self.screen = scr                                                       #La fenetre qui est ouverte
        self.screenWidth = sWidth
        self.screenHeight = sHeight
        self.currentScene = MainMenuScene(self)                                 #La scene qui est affiche en premier


    def update(self):
        self.currentScene.update()                                              #Update la scene en cours
        pass

    def draw(self):
        self.currentScene.draw(self.screen)                                     #Dessine la scene en cours
        pygame.display.flip()                                                   #Affiche sur la fenetre ce que l'on vient dessiner
        pass

    def onEvent(self, event):
        self.currentScene.onEvent(event)                                        #Recupere les Events
        pass

    def changeScene(self, newScene):
        self.currentScene = newScene                                            #Permet de changer de scene avec les animations
