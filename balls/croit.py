from components.ball import Ball


class CroitBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "croit_spritesheet_yellow.png"
        self.red_spritesheet = "croit_spritesheet_red.png"
        self.blue_spritesheet = "croit_spritesheet_blue.png"
        self.pink_spritesheet = "croit_spritesheet_pink.png"
        self.blue2_spritesheet = "croit_spritesheet_blue2.png"
        self.green_spritesheet = "croit_spritesheet_green.png"

        self.price = 5
        self.selected = False
        self.numFrames = 9
        self.speed = 0.02
        self.id = 1
        self.name = "BasicBall"
