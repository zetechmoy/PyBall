#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------
#MainMenuScene est le scene qui est affichee lorsqu'on demarre le jeu, c'est la scene qui permet de choisir entre jouer, changer de balle etc...
import pygame, sys
from pygame.locals import *
from Scene import Scene
import Helper

import GameScene                                                                #Si on fait from GameScene import GameScene ca fait un import cyclique donc ca marche pas
import BallScene

import ScoreManager
import Colors
import Constants
import Language
import ValueManager
from Language import getLang

class MainMenuScene(Scene):

    def __init__(self, gmp):
        pygame.init()                                                           #Initialise pygame
        self.gamePanel = gmp
		#bouton de debut de jeu
        self.startbutton = pygame.transform.scale(                              #Creer une image
            pygame.image.load("./drawable/startbutton.png").convert_alpha(),    #et la redimensionne
            (int(self.gamePanel.screenHeight/6),int(self.gamePanel.screenHeight/6))
        )
        self.startButtonPos = (self.gamePanel.screenWidth/2 - int(self.gamePanel.screenHeight/12),
            self.gamePanel.screenHeight/2 - int(self.gamePanel.screenHeight/12))
		#bouton pour quitter le jeu
        self.quitbutton = pygame.transform.scale(                              #Creer une image
            pygame.image.load("./drawable/quit.png").convert_alpha(),    #et la redimensionne
            (int(self.gamePanel.screenHeight/12),int(self.gamePanel.screenHeight/12))
        )
        self.quitButtonPos = (self.gamePanel.screenWidth - self.quitbutton.get_rect()[3] - 10, 10)

		#bouton pour le magasin
        self.shopButton = pygame.transform.scale(                              #Creer une image
            pygame.image.load("./drawable/ballscene_button.png").convert_alpha(),    #et la redimensionne
            (int(self.gamePanel.screenHeight/6),int(self.gamePanel.screenHeight/6))
        )
        self.shopButtonPos = (self.gamePanel.screenWidth/2 - int(self.gamePanel.screenHeight/12),
            self.gamePanel.screenHeight/2 - int(self.gamePanel.screenHeight/12) + int(self.gamePanel.screenHeight/4))

        self.balltitle = pygame.image.load("./drawable/balltitle.png").convert_alpha()#Creer une image pour le titre
        self.ballTitlePos = (self.gamePanel.screenWidth/2 - self.balltitle.get_rect()[2]/2, 0)

        self.font = pygame.font.Font("./fonts/Hero.otf", 30)
        self.scoreText = self.font.render("{} {}".format(Language.high_score[getLang()],ScoreManager.get()), 1, Colors.deep_purple)
        self.scoreTextPos = self.scoreText.get_rect()
        self.scoreTextPos.x = self.gamePanel.screenWidth/2 - self.scoreText.get_rect()[2]/2
        self.scoreTextPos.y = (self.startButtonPos[1] - (self.ballTitlePos[1] + self.balltitle.get_rect()[3]))/2 - self.scoreTextPos.height/2 + (self.ballTitlePos[1] + self.balltitle.get_rect()[3])

    def onEvent(self, event):
         if event.type == pygame.MOUSEBUTTONUP:                                 #Si le type l'event est un click vers le haut
            pos = pygame.mouse.get_pos()                                        #Recupere la position du click


            if Helper.clickIsInRect(pos, self.startbutton.get_rect(), self.startButtonPos):#Si le click ce trouve dans le rectangle du bouton start
                self.gamePanel.changeScene(GameScene.GameScene(self.gamePanel)) #On change la scene en cours avec la scene GameScene

            if Helper.clickIsInRect(pos, self.shopButton.get_rect(), self.shopButtonPos):#Si le click ce trouve dans le rectangle du bouton shop
                self.gamePanel.changeScene(BallScene.BallScene(self.gamePanel)) #On change la scene en cours avec la scene BallScene

            if Helper.clickIsInRect(pos, self.quitbutton.get_rect(), self.quitButtonPos):#Si le click ce trouve dans le rectangle du bouton quit
                ValueManager.save("FPS", str(Constants.FPS))
                pygame.quit()                                                   #On quit le jeu
                sys.exit()
##         if event.type == KEYDOWN:
##            if event.key == K_ESCAPE:
##                pygame.quit()                                                   #On quite le jeu
##                sys.exit()
            #SI ON DOIT CLICKER SUR DES TRUCS QUI SE SUPERPOSENT,
            #ON DOIT FAIRE TESTER LES PLUS PETITS ELEMENTS EN PREMIER


    def update(self):
        #super(MainMenuScene, self).update()                                    #Appelle la fonction update() de la superclass Scene
        self.scoreText = self.font.render("{} {}".format(Language.high_score[getLang()],ScoreManager.get()), 1, Colors.deep_purple)


    def draw(self, fen):
        fen.fill(Colors.white)                                               #Dessine le background aux coordonnees (0,0)
        fen.blit(self.balltitle, self.ballTitlePos)                                         #Dessine le titre (0,0)
        fen.blit(self.startbutton, self.startButtonPos)
        fen.blit(self.shopButton, self.shopButtonPos)                                  #Dessine le bouton de start aux coordonnees :
                                                                                #400/2 - ((400/4)/2), 600/2 - ((400/4)/2)
        fen.blit(self.quitbutton, self.quitButtonPos)
        fen.blit(self.scoreText, self.scoreTextPos)
        super(MainMenuScene, self).update()
