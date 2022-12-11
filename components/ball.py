# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------

# Definit les caracteristiques des balles

# Toutes les balles tournes. L'effet est donne en decoupant les balles tres precisement puis affiche tres vite a la suite.
# Le fait de les afficher tres vite a la suite va faire que le cerveau va interpreter une rotation
# voir Animation.py pour gestion de l'animation de rotation

from abc import ABC


class Ball(ABC):

    yellow_spritesheet = "default_spritesheet_yellow.png"  # Sprite pour le theme Yellow
    red_spritesheet = "default_spritesheet_red.png"  # Sprite pour le theme Red
    blue_spritesheet = "default_spritesheet_blue.png"  # Sprite pour le theme Blue
    pink_spritesheet = "default_spritesheet_pink.png"  # Sprite pour le theme Pink
    blue2_spritesheet = "default_spritesheet_blue2.png"  # Sprite pour le theme blue2
    green_spritesheet = "default_spritesheet_green.png"  # Sprite pour le theme green
    price = 0  # Prix de la balle
    selected = True  # Selectionnee par defaut
    numFrames = 6  # Nb de frames par sprite
    speed = 0.03  # Speed de rotation en s
    id = 0  # Id de la balle pour la gestion
    name = "DefaultBall"  # Nom de la balle
