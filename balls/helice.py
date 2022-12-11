from components.ball import Ball


class HeliceBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "helice_spritesheet_yellow.png"
        self.red_spritesheet = "helice_spritesheet_red.png"
        self.blue_spritesheet = "helice_spritesheet_blue.png"
        self.pink_spritesheet = "helice_spritesheet_pink.png"
        self.blue2_spritesheet = "helice_spritesheet_blue2.png"
        self.green_spritesheet = "helice_spritesheet_green.png"

        self.price = 300
        self.selected = True
        self.numFrames = 9
        self.speed = 0.02
        self.id = 7
        self.name = "CoolBall2"
