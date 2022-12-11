from components.ball import Ball


class DefaultBall(Ball):
    def __init__(self):
        self.yellow_spritesheet = (
            "default_spritesheet_yellow.png"  # Sprite pour le theme Yellow
        )
        self.red_spritesheet = "default_spritesheet_red.png"  # Sprite pour le theme Red
        self.blue_spritesheet = (
            "default_spritesheet_blue.png"  # Sprite pour le theme Blue
        )
        self.pink_spritesheet = (
            "default_spritesheet_pink.png"  # Sprite pour le theme Pink
        )
        self.blue2_spritesheet = (
            "default_spritesheet_blue2.png"  # Sprite pour le theme blue2
        )
        self.green_spritesheet = (
            "default_spritesheet_green.png"  # Sprite pour le theme green
        )

        self.price = 0  # Prix de la balle
        self.selected = True  # Selectionnee par defaut
        self.numFrames = 6  # Nb de frames par sprite
        self.speed = 0.03  # Speed de rotation en s
        self.id = 0  # Id de la balle pour la gestion
        self.name = "DefaultBall"  # Nom de la balle
