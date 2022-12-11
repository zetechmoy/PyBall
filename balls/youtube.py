from components.ball import Ball


class YoutubeBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = "youtube_spritesheet_yellow.png"
        self.red_spritesheet = "youtube_spritesheet_red.png"
        self.blue_spritesheet = "youtube_spritesheet_blue.png"
        self.pink_spritesheet = "youtube_spritesheet_pink.png"
        self.blue2_spritesheet = "youtube_spritesheet_blue2.png"
        self.green_spritesheet = "youtube_spritesheet_green.png"

        self.price = 100
        self.selected = True
        self.numFrames = 8
        self.speed = 0.02
        self.id = 14
        self.name = "YoutubeBall"
