from components.ball import Ball


class TennisBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "tennis_spritesheet_yellow.png"
        self.red_spritesheet = "tennis_spritesheet_red.png"
        self.blue_spritesheet = "tennis_spritesheet_blue.png"
        self.pink_spritesheet = "tennis_spritesheet_pink.png"
        self.blue2_spritesheet = "tennis_spritesheet_blue2.png"
        self.green_spritesheet = "tennis_spritesheet_green.png"

        self.price = 200
        self.selected = True
        self.numFrames = 8
        self.speed = 0.02
        self.id = 11
        self.name = "TennisBall"
