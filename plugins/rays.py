# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	09/12/2022
# -------------------------------------------------------------------------------

import random, pygame, Constants, components.helper as helper, os
import gc
from components.plugin import Plugin
from components.rays import Rays
from sys import getrefcount


class RaysPlugin(Plugin):
    def __init__(self):
        self.platforms = dict()
        self.player = None
        self.nb_rays = 10

        self.rays = list()
        self.closest_intersections = list()

        self.currentSceneName = None

    def update(self):
        if self.player:

            print("{}, platforms: {}".format(id(self.platforms), len(self.platforms)))
            self.rays = Rays.getRaysCoordinates(self.player, self.nb_rays)
            self.closest_intersections = Rays.getRaysClosestIntersection(
                self.rays, self.platforms
            )

        super(RaysPlugin, self).update()

    def draw(self, fen):
        if (
            self.player
            and self.player["isPlaying"]
            and self.currentSceneName == "GameScene"
        ):
            for ray in self.rays:
                pygame.draw.line(fen, (255, 0, 0), ray[0], ray[1], ray[2])

            for intersection in self.closest_intersections:
                pygame.draw.circle(fen, (0, 255, 0), intersection[1], 5)
        super(RaysPlugin, self).draw(fen)

    def onEvent(self, event):
        if event.type == Constants.PLAYER_MOVE_EVENT:
            data = event.__dict__
            # print("Player move event in plugin: {}, {}, {}".format(data["id"], data["x"], data["y"]))
            self.player = data

        if event.type == Constants.PLATFORM_MOVE_EVENT:
            data = event.__dict__
            # print("Platform move event in plugin: {}, {}, {}".format(data["id"], data["x"], data["y"]))
            # if data["id"] not in self.platforms:
            self.platforms[data["id"]] = data

        if event.type == Constants.PLATFORM_DELETE_EVENT:
            data = event.__dict__
            # print("Platform delete event in plugin: {}, {}, {}".format(data["id"], data["x"], data["y"]))
            if data["id"] in self.platforms:
                del self.platforms[data["id"]]

        if event.type == Constants.PLAYER_DELETE_EVENT:
            self.player = None

        if event.type == Constants.PLAYER_CREATED_EVENT:
            data = event.__dict__
            self.player = data

        if event.type == Constants.END_EVENT:
            print("End event in plugin")
            self.rays.clear()
            self.platforms.clear()
            self.player = None
            print(getrefcount(self.platforms))
            print("{}, platforms: {}".format(id(self.platforms), len(self.platforms)))
            self.update()

        if event.type == Constants.CHANGE_SCENE_EVENT:
            data = event.__dict__
            self.currentSceneName = data["name"]

        super(RaysPlugin, self).onEvent(event)
