from components.ball import Ball


class CoolBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "cool_ball_yellow.png"
        self.red_spritesheet = "cool_ball_red.png"
        self.blue_spritesheet = "cool_ball_blue.png"
        self.pink_spritesheet = "cool_ball_pink.png"
        self.blue2_spritesheet = "cool_ball_blue2.png"
        self.green_spritesheet = "cool_ball_green.png"

        self.price = 20
        self.selected = True
        self.numFrames = 9
        self.speed = 0.02
        self.id = 4
        self.name = "CoolBall"
