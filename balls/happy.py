from components.ball import Ball


class HappyBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "happy_spritesheet_yellow.png"
        self.red_spritesheet = "happy_spritesheet_red.png"
        self.blue_spritesheet = "happy_spritesheet_blue.png"
        self.pink_spritesheet = "happy_spritesheet_pink.png"
        self.blue2_spritesheet = "happy_spritesheet_blue2.png"
        self.green_spritesheet = "happy_spritesheet_green.png"

        self.price = 200
        self.selected = True
        self.numFrames = 12
        self.speed = 0.02
        self.id = 6
        self.name = "HappyBall"
