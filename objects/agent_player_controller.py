import random, Constants, components.helper as helper, os

from components.player_controller import PlayerController
from components.rays import Rays
from objects.player import Player


class AgentPlayerController(PlayerController):
    def __init__(self, initPlayerPos):
        super(AgentPlayerController, self).__init__()
        self.movingUp = False

        self.platforms = dict()
        self.player = None
        self.nb_rays = 10

        self.rays = list()
        self.closest_intersections = list()
        self.player_pos = initPlayerPos
        self.player_score = 0

    def onEvent(self, event):
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

        if event.type == Constants.SCORE_UPDATE_EVENT:
            data = event.__dict__
            # print("Score update event in plugin: {}, {}, {}".format(data["id"], data["x"], data["y"]))
            self.player_score = data["score"]

        if event.type == Constants.END_EVENT:
            self.player_score = self.player_score - 15

        if event.type == Constants.PLAYER_CREATED_EVENT:
            data = event.__dict__
            self.player_pos = [data["x"], data["y"]]

        return super(AgentPlayerController, self).onEvent(event)

    def onEventWithPlayer(self, event, player):
        self.rays = Rays.getRaysCoordinates(player, self.nb_rays)
        self.closest_intersections = Rays.getRaysClosestIntersection(
            self.rays, self.platforms
        )

        if isinstance(player, Player):
            self.player_pos = [player.pos.x, player.pos.y]
        else:
            self.player_pos = [player["x"], player["y"]]

        # self.last_state = [norm_x, norm_y] + [x[0] for x in self.closest_intersections]
        # print(self.last_state)

        return super(AgentPlayerController, self).onEventWithPlayer(event, player)

    def getState(self):
        norm_x = self.player_pos[0] / Constants.screenWidth
        norm_y = self.player_pos[1] / Constants.screenHeight

        return [norm_x, norm_y] + [x[0] for x in self.closest_intersections]

    def decideUpOrDown(self):
        state = self.getState()
        # print("decideUpOrDown: ", state)
        return random.choice([True, False])
