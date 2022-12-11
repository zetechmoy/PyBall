from components.ball import Ball


class StarBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "star_spritesheet_yellow.png"
        self.red_spritesheet = "star_spritesheet_red.png"
        self.blue_spritesheet = "star_spritesheet_blue.png"
        self.pink_spritesheet = "star_spritesheet_pink.png"
        self.blue2_spritesheet = "star_spritesheet_blue2.png"
        self.green_spritesheet = "star_spritesheet_green.png"

        self.price = 200
        self.selected = True
        self.numFrames = 8
        self.speed = 0.02
        self.id = 9
        self.name = "StarBall"
