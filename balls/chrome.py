from components.ball import Ball


class ChromeBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "chrome_spritesheet_yellow.png"
        self.red_spritesheet = "chrome_spritesheet_red.png"
        self.blue_spritesheet = "chrome_spritesheet_blue.png"
        self.pink_spritesheet = "chrome_spritesheet_pink.png"
        self.blue2_spritesheet = "chrome_spritesheet_blue2.png"
        self.green_spritesheet = "chrome_spritesheet_green.png"

        self.price = 50
        self.selected = True
        self.numFrames = 12
        self.speed = 0.02
        self.id = 3
        self.name = "ChromeBall"
