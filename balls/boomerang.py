from components.ball import Ball


class BoomerangBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "boomerang_spritesheet_yellow.png"
        self.red_spritesheet = "boomerang_spritesheet_red.png"
        self.blue_spritesheet = "boomerang_spritesheet_blue.png"
        self.pink_spritesheet = "boomerang_spritesheet_pink.png"
        self.blue2_spritesheet = "boomerang_spritesheet_blue2.png"
        self.green_spritesheet = "boomerang_spritesheet_green.png"

        self.price = 150
        self.selected = False
        self.numFrames = 8
        self.speed = 0.02
        self.id = 2
        self.name = "BoomerangBall"
