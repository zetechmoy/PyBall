from pygame import K_SPACE, KEYDOWN, KEYUP

from components.player_controller import PlayerController


class KeyboardPlayerController(PlayerController):
    def __init__(self):
        super(KeyboardPlayerController, self).__init__()
        self.movingUp = False

    def onEvent(self, event):
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                self.movingUp = True

        elif event.type == KEYUP:
            if event.key == K_SPACE:
                self.movingUp = False

        return super(KeyboardPlayerController, self).onEvent(event)

    def decideUpOrDown(self):
        return self.movingUp
