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
        self.plugins = list()                                                       #Les plugins qui sont actifs

    def update(self):
        self.currentScene.update()                                              #Update la scene en cours
        for plugin in self.plugins:
            plugin.update()                                                     #Update les plugins

    def draw(self):
        self.currentScene.draw(self.screen)                                     #Dessine la scene en cours
        for plugin in self.plugins:
            plugin.draw(self.screen)                                            #Dessine les plugins
        pygame.display.flip()                                                   #Affiche sur la fenetre ce que l'on vient dessiner
        
    def onEvent(self, event):
        self.currentScene.onEvent(event)                                        #Recupere les Events
        for plugin in self.plugins:
            plugin.onEvent(event)                                                 #Recupere les Events des plugins

    def changeScene(self, newScene):
        self.currentScene = newScene                                            #Permet de changer de scene avec les animations

    def addPlugin(self, plugin):
        self.plugins.append(plugin)                                             #Permet d'ajouter un plugin a la scene en cours

    def resetPlugins(self):
        self.plugins = list()