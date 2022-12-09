#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

#Definit les caracteristiques des balles

#Toutes les balles tournes. L'effet est donne en decoupant les balles tres precisement puis affiche tres vite a la suite.
#Le fait de les afficher tres vite a la suite va faire que le cerveau va interpreter une rotation
#voir Animation.py pour gestion de l'animation de rotation

class DefaultBall:
    def __init__(self):
        self.yellow_spritesheet =   "default_spritesheet_yellow.png" 	#Sprite pour le theme Yellow
        self.red_spritesheet =      "default_spritesheet_red.png"		#Sprite pour le theme Red
        self.blue_spritesheet =     "default_spritesheet_blue.png"		#Sprite pour le theme Blue
        self.pink_spritesheet =     "default_spritesheet_pink.png"		#Sprite pour le theme Pink
        self.blue2_spritesheet =    "default_spritesheet_blue2.png"		#Sprite pour le theme blue2
        self.green_spritesheet =    "default_spritesheet_green.png"		#Sprite pour le theme green

        self.price = 0													#Prix de la balle
        self.selected = True											#Selectionnee par defaut
        self.numFrames = 6												#Nb de frames par sprite
        self.speed = 0.03												#Speed de rotation en s
        self.id = 0														#Id de la balle pour la gestion
        self.name = "DefaultBall"										#Nom de la balle

class CroitBall:
    def __init__(self):
        self.yellow_spritesheet =   "croit_spritesheet_yellow.png"
        self.red_spritesheet =      "croit_spritesheet_red.png"
        self.blue_spritesheet =     "croit_spritesheet_blue.png"
        self.pink_spritesheet =     "croit_spritesheet_pink.png"
        self.blue2_spritesheet =    "croit_spritesheet_blue2.png"
        self.green_spritesheet =    "croit_spritesheet_green.png"

        self.price = 5
        self.selected = False
        self.numFrames = 9
        self.speed = 0.02
        self.id = 1
        self.name = "BasicBall"

class BoomerangBall:
    def __init__(self):
        self.yellow_spritesheet =   "boomerang_spritesheet_yellow.png"
        self.red_spritesheet =      "boomerang_spritesheet_red.png"
        self.blue_spritesheet =     "boomerang_spritesheet_blue.png"
        self.pink_spritesheet =     "boomerang_spritesheet_pink.png"
        self.blue2_spritesheet =    "boomerang_spritesheet_blue2.png"
        self.green_spritesheet =    "boomerang_spritesheet_green.png"

        self.price = 150
        self.selected = False
        self.numFrames = 8
        self.speed = 0.02
        self.id = 2
        self.name = "BoomerangBall"

class ChromeBall:
    def __init__(self):
        self.yellow_spritesheet =   "chrome_spritesheet_yellow.png"
        self.red_spritesheet =      "chrome_spritesheet_red.png"
        self.blue_spritesheet =     "chrome_spritesheet_blue.png"
        self.pink_spritesheet =     "chrome_spritesheet_pink.png"
        self.blue2_spritesheet =    "chrome_spritesheet_blue2.png"
        self.green_spritesheet =    "chrome_spritesheet_green.png"

        self.price = 50
        self.selected = True
        self.numFrames = 12
        self.speed = 0.02
        self.id = 3
        self.name = "ChromeBall"

class CoolBall:
    def __init__(self):
        self.yellow_spritesheet =   "cool_ball_yellow.png"
        self.red_spritesheet =      "cool_ball_red.png"
        self.blue_spritesheet =     "cool_ball_blue.png"
        self.pink_spritesheet =     "cool_ball_pink.png"
        self.blue2_spritesheet =    "cool_ball_blue2.png"
        self.green_spritesheet =    "cool_ball_green.png"

        self.price = 20
        self.selected = True
        self.numFrames = 9
        self.speed = 0.02
        self.id = 4
        self.name = "CoolBall"

class EllipseBall:
    def __init__(self):
        self.yellow_spritesheet =   "ellipse_spritesheet_yellow.png"
        self.red_spritesheet =      "ellipse_spritesheet_red.png"
        self.blue_spritesheet =     "ellipse_spritesheet_blue.png"
        self.pink_spritesheet =     "ellipse_spritesheet_pink.png"
        self.blue2_spritesheet =    "ellipse_spritesheet_blue2.png"
        self.green_spritesheet =    "ellipse_spritesheet_green.png"

        self.price = 100
        self.selected = True
        self.numFrames = 7
        self.speed = 0.02
        self.id = 5
        self.name = "EllipseBall"

class HappyBall:
    def __init__(self):
        self.yellow_spritesheet =   "happy_spritesheet_yellow.png"
        self.red_spritesheet =      "happy_spritesheet_red.png"
        self.blue_spritesheet =     "happy_spritesheet_blue.png"
        self.pink_spritesheet =     "happy_spritesheet_pink.png"
        self.blue2_spritesheet =    "happy_spritesheet_blue2.png"
        self.green_spritesheet =    "happy_spritesheet_green.png"

        self.price = 200
        self.selected = True
        self.numFrames = 12
        self.speed = 0.02
        self.id = 6
        self.name = "HappyBall"

class HeliceBall:
    def __init__(self):
        self.yellow_spritesheet =   "helice_spritesheet_yellow.png"
        self.red_spritesheet =      "helice_spritesheet_red.png"
        self.blue_spritesheet =     "helice_spritesheet_blue.png"
        self.pink_spritesheet =     "helice_spritesheet_pink.png"
        self.blue2_spritesheet =    "helice_spritesheet_blue2.png"
        self.green_spritesheet =    "helice_spritesheet_green.png"

        self.price = 300
        self.selected = True
        self.numFrames = 9
        self.speed = 0.02
        self.id = 7
        self.name = "CoolBall2"

class RadioactifBall:
    def __init__(self):
        self.yellow_spritesheet =   "radio_spritesheet_yellow.png"
        self.red_spritesheet =      "radio_spritesheet_red.png"
        self.blue_spritesheet =     "radio_spritesheet_blue.png"
        self.pink_spritesheet =     "radio_spritesheet_pink.png"
        self.blue2_spritesheet =    "radio_spritesheet_blue2.png"
        self.green_spritesheet =    "radio_spritesheet_green.png"

        self.price = 50
        self.selected = True
        self.numFrames = 12
        self.speed = 0.02
        self.id = 8
        self.name ="RadioactifBall"

class StarBall:
    def __init__(self):
        self.yellow_spritesheet =   "star_spritesheet_yellow.png"
        self.red_spritesheet =      "star_spritesheet_red.png"
        self.blue_spritesheet =     "star_spritesheet_blue.png"
        self.pink_spritesheet =     "star_spritesheet_pink.png"
        self.blue2_spritesheet =    "star_spritesheet_blue2.png"
        self.green_spritesheet =    "star_spritesheet_green.png"

        self.price = 200
        self.selected = True
        self.numFrames = 8
        self.speed = 0.02
        self.id = 9
        self.name = "StarBall"

class SuperBall:
    def __init__(self):
        self.yellow_spritesheet =   "super_spritesheet_yellow.png"
        self.red_spritesheet =      "super_spritesheet_red.png"
        self.blue_spritesheet =     "super_spritesheet_blue.png"
        self.pink_spritesheet =     "super_spritesheet_pink.png"
        self.blue2_spritesheet =    "super_spritesheet_blue2.png"
        self.green_spritesheet =    "super_spritesheet_green.png"

        self.price = 750
        self.selected = True
        self.numFrames = 12
        self.speed = 0.02
        self.id = 10
        self.name = "SuperBall"

class TennisBall:
    def __init__(self):
        self.yellow_spritesheet =   "tennis_spritesheet_yellow.png"
        self.red_spritesheet =      "tennis_spritesheet_red.png"
        self.blue_spritesheet =     "tennis_spritesheet_blue.png"
        self.pink_spritesheet =     "tennis_spritesheet_pink.png"
        self.blue2_spritesheet =    "tennis_spritesheet_blue2.png"
        self.green_spritesheet =    "tennis_spritesheet_green.png"

        self.price = 200
        self.selected = True
        self.numFrames = 8
        self.speed = 0.02
        self.id = 11
        self.name = "TennisBall"

class TimeBall:
    def __init__(self):
        self.yellow_spritesheet =   "timeball_spritesheet_yellow.png"
        self.red_spritesheet =      "timeball_spritesheet_red.png"
        self.blue_spritesheet =     "timeball_spritesheet_blue.png"
        self.pink_spritesheet =     "timeball_spritesheet_pink.png"
        self.blue2_spritesheet =    "timeball_spritesheet_blue2.png"
        self.green_spritesheet =    "timeball_spritesheet_green.png"

        self.price = 20
        self.selected = True
        self.numFrames = 6
        self.speed = 0.02
        self.id = 12
        self.name = "TimeBall"

class UbiBall:
    def __init__(self):
        self.yellow_spritesheet =   "ubi_spritesheet_yellow.png"
        self.red_spritesheet =      "ubi_spritesheet_red.png"
        self.blue_spritesheet =     "ubi_spritesheet_blue.png"
        self.pink_spritesheet =     "ubi_spritesheet_pink.png"
        self.blue2_spritesheet =    "ubi_spritesheet_blue2.png"
        self.green_spritesheet =    "ubi_spritesheet_green.png"

        self.price = 200
        self.selected = True
        self.numFrames = 8
        self.speed = 0.02
        self.id = 13
        self.name = "UbiBall"

class YoutubeBall:
    def __init__(self):
        self.yellow_spritesheet =   "youtube_spritesheet_yellow.png"
        self.red_spritesheet =      "youtube_spritesheet_red.png"
        self.blue_spritesheet =     "youtube_spritesheet_blue.png"
        self.pink_spritesheet =     "youtube_spritesheet_pink.png"
        self.blue2_spritesheet =    "youtube_spritesheet_blue2.png"
        self.green_spritesheet =    "youtube_spritesheet_green.png"

        self.price = 100
        self.selected = True
        self.numFrames = 8
        self.speed = 0.02
        self.id = 14
        self.name = "YoutubeBall"

def getBalls():	#Retourne une liste de balles, il faut la rajouter a la liste si vous voulez qu'elle soit affichee
    t = [DefaultBall(), CroitBall(), BoomerangBall(), ChromeBall(), CoolBall(),
     EllipseBall(), HappyBall(), HeliceBall(), RadioactifBall(), StarBall(), SuperBall(), TennisBall(),
     TimeBall(), UbiBall(), YoutubeBall()]
    return t
