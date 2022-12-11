import random
from components.object import Object


class PlayerController(Object):
    def onEvent(self, event):
        return super(PlayerController, self).onEvent(event)

    def onEventWithPlayer(self, event, player):
        pass

    def decideUpOrDown(self):
        return random.choice([True, False])
