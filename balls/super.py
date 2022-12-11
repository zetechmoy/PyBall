from components.ball import Ball


class SuperBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "super_spritesheet_yellow.png"
        self.red_spritesheet = "super_spritesheet_red.png"
        self.blue_spritesheet = "super_spritesheet_blue.png"
        self.pink_spritesheet = "super_spritesheet_pink.png"
        self.blue2_spritesheet = "super_spritesheet_blue2.png"
        self.green_spritesheet = "super_spritesheet_green.png"

        self.price = 750
        self.selected = True
        self.numFrames = 12
        self.speed = 0.02
        self.id = 10
        self.name = "SuperBall"
