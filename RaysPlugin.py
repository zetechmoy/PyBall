#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	09/12/2022
#-------------------------------------------------------------------------------

import random, pygame, Constants, Helper, os

class RaysPlugin:

    def __init__(self):
        self.platforms = dict()
        self.player = None
        self.nb_rays = 10

    def update(self):
        pass

    def draw(self, fenetre):
        if self.player:
            for i in range(self.nb_rays):
                angle = i * 180 / self.nb_rays - 90 + 90 / self.nb_rays
                x = self.player["x"] + self.player["width"] / 2
                y = self.player["y"] + self.player["height"] / 2
                
                # draw ray
                lineFrom = (x, y)
                lineTo = Helper.getPointAtAngle(x, y, angle, 1000)
                lineWeight = 5
                pygame.draw.line(fenetre, (255, 0, 0), lineFrom, lineTo, lineWeight)

                # draw intersection
                for platform in self.platforms.values():
                    # compute intersection between ray and platform
                    intersections = Helper.getIntersections(lineFrom, lineTo, platform["x"], platform["y"], platform["width"], platform["height"])
                    for intersection in intersections:
                        pygame.draw.circle(fenetre, (0, 255, 0), intersection, 5)      

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

        if event.type == Constants.END_EVENT:
            self.platforms = dict()
            self.player = None
            
            