# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	09/12/2022
# -------------------------------------------------------------------------------

import random, pygame, Constants, components.helper as helper, os

from components.plugin import Plugin


class StopPlugin(Plugin):
    def __init__(self, playerController, onStop):
        self.playerController = playerController
        self.onStop = onStop
        self.score = 0

    def onEvent(self, event):
        if event.type == Constants.END_EVENT:
            state = self.playerController.getState()
            self.onStop(state, self.score)

            # Reset score
            self.score = 0

        if event.type == Constants.SCORE_UPDATE_EVENT:
            self.score = event.score

        super(StopPlugin, self).onEvent(event)
