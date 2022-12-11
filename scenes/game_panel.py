# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------
from typing import List
import pygame
import Constants
from components.plugin import Plugin
from components.scene import Scene

from scenes.main_menu_scene import MainMenuScene
from scenes.game_scene import GameScene
from copy import deepcopy


class GamePanel(Scene):
    def __init__(self, scr, sWidth, sHeight, player=None, initScene=None):
        self.screen = scr  # La fenetre qui est ouverte
        self.screenWidth = sWidth
        self.screenHeight = sHeight
        self.currentScene = (
            initScene if initScene else MainMenuScene(self)
        )  # La scene qui est affiche en premier
        self.beforePlugins: List[Plugin] = list()  # Les plugins qui sont actifs
        self.afterPlugins: List[Plugin] = list()  # Les plugins qui sont actifs
        self.player = player

    def update(self):
        for plugin in self.beforePlugins:
            plugin.update()

        self.currentScene.update()

        for plugin in self.afterPlugins:
            plugin.update()

        super(GamePanel, self).update()

    def draw(self):

        for plugin in self.beforePlugins:
            plugin.draw(self.screen)

        self.currentScene.draw(self.screen)

        for plugin in self.afterPlugins:
            plugin.draw(self.screen)

        super(GamePanel, self).draw(self.screen)

        # Affiche sur la fenetre ce que l'on vient dessiner
        pygame.display.flip()

    def onEvent(self, event):

        for plugin in self.beforePlugins:
            plugin.onEvent(event)

        # Recupere les Events
        self.currentScene.onEvent(event)

        for plugin in self.afterPlugins:
            plugin.onEvent(event)

        super(GamePanel, self).onEvent(event)

    def changeScene(self, newScene):
        self.currentScene = newScene  # Permet de changer de scene avec les animations

        sceneEvent = pygame.event.Event(
            Constants.CHANGE_SCENE_EVENT, {"name": self.currentScene.__class__.__name__}
        )
        pygame.event.post(sceneEvent)

    def registerPlugin(self, plugin, when="after"):
        if when == "before":
            self.beforePlugins.append(plugin)
        elif when == "after":
            self.afterPlugins.append(plugin)

    def resetPlugins(self):
        self.beforePlugins = list()
        self.afterPlugins = list()
