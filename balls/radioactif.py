from components.ball import Ball


class RadioactifBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "radio_spritesheet_yellow.png"
        self.red_spritesheet = "radio_spritesheet_red.png"
        self.blue_spritesheet = "radio_spritesheet_blue.png"
        self.pink_spritesheet = "radio_spritesheet_pink.png"
        self.blue2_spritesheet = "radio_spritesheet_blue2.png"
        self.green_spritesheet = "radio_spritesheet_green.png"

        self.price = 50
        self.selected = True
        self.numFrames = 12
        self.speed = 0.02
        self.id = 8
        self.name = "RadioactifBall"
