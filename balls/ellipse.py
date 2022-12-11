from components.ball import Ball


class EllipseBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "ellipse_spritesheet_yellow.png"
        self.red_spritesheet = "ellipse_spritesheet_red.png"
        self.blue_spritesheet = "ellipse_spritesheet_blue.png"
        self.pink_spritesheet = "ellipse_spritesheet_pink.png"
        self.blue2_spritesheet = "ellipse_spritesheet_blue2.png"
        self.green_spritesheet = "ellipse_spritesheet_green.png"

        self.price = 100
        self.selected = True
        self.numFrames = 7
        self.speed = 0.02
        self.id = 5
        self.name = "EllipseBall"
