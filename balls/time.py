from components.ball import Ball


class TimeBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "timeball_spritesheet_yellow.png"
        self.red_spritesheet = "timeball_spritesheet_red.png"
        self.blue_spritesheet = "timeball_spritesheet_blue.png"
        self.pink_spritesheet = "timeball_spritesheet_pink.png"
        self.blue2_spritesheet = "timeball_spritesheet_blue2.png"
        self.green_spritesheet = "timeball_spritesheet_green.png"

        self.price = 20
        self.selected = True
        self.numFrames = 6
        self.speed = 0.02
        self.id = 12
        self.name = "TimeBall"
