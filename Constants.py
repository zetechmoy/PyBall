# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------

import pygame

from themes.yellow import YellowGameTheme

FPS = 30  # Nombre de frame par seconde du jeu conseil (60/90) le jeu devient plus difficile, cette valeur depend des capacites de votre machine
screenSize = (400, 600)  # Taille de la fenetre (sera en fullscreen par la suite)
screenHeight = 450
screenWidth = 800
screenRect = pygame.Rect(0, 0, 400, 600)  # Objet Rect de la fenetre
timeBetween2Bonus = 7  # s				#Temps entre chaques bonus
initTheme = YellowGameTheme()


# Events
PLAYER_MOVE_EVENT = pygame.USEREVENT + 1
PLATFORM_MOVE_EVENT = pygame.USEREVENT + 2
PLATFORM_DELETE_EVENT = pygame.USEREVENT + 3
PLAYER_DELETE_EVENT = pygame.USEREVENT + 4
END_EVENT = pygame.USEREVENT + 5
START_EVENT = pygame.USEREVENT + 6
NEW_GAME_THEME_EVENT = pygame.USEREVENT + 7
SCORE_UPDATE_EVENT = pygame.USEREVENT + 8
PLAYER_CREATED_EVENT = pygame.USEREVENT + 9
CHANGE_SCENE_EVENT = pygame.USEREVENT + 10
