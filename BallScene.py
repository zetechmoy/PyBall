# -*- coding: utf-8 -*-

#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

import pygame, math

from Scene import Scene

import MainMenuScene, Constants, Colors, Helper, Balls

from BallView import BallView

class BallScene(Scene):
    def __init__(self, gmp):

        pygame.init()

        self.gamePanel = gmp

        self.mousePressed = False
        self.lastPos = (0, 0)
        self.dy = 0

        self.backButton = pygame.transform.scale(
            pygame.image.load("./drawable/back.png").convert_alpha(),
            (int(self.gamePanel.screenHeight/12),int(self.gamePanel.screenHeight/12))
        )

        self.backButtonPos = (10, 10)

        self.font = pygame.font.Font("./fonts/Hero.otf", 24)

        self.piece = pygame.image.load('./drawable/circle_yellow.png').convert_alpha()
        self.coinText = self.font.render(Helper.getCoin(), 1, Colors.yellow)
        self.coinTextPos = self.coinText.get_rect()
        self.coinTextPos.x = self.gamePanel.screenWidth/2 - int(self.coinTextPos.width / 2) - 1
        self.piece = pygame.transform.scale(self.piece, (self.coinTextPos.height, self.coinTextPos.height))
        self.piecePos = self.piece.get_rect()
        self.piecePos.x = self.coinTextPos.x + self.coinTextPos.width + 1
        self.piecePos.y = 5
        self.coinTextPos.y = 7

        self.ballViews = []
        bvx, bvy = 0, -self.gamePanel.screenHeight/4
        for i in range(0, len(Balls.getBalls())):
            if(i%2==0):
                bvx = 0
                bvy += self.gamePanel.screenHeight/4
            else:
                bvx = int(self.gamePanel.screenWidth/2)

            self.ballViews.append(BallView(self.gamePanel, Balls.getBalls()[i], bvx, bvy))


        self.refreshPaidBalls()

        selectedBall = int(Helper.getSelectedBall())
        for b in self.ballViews:
            if(b.ball.id == selectedBall):
                b.selected = True


    def onEvent(self, event):
        if event.type == pygame.MOUSEBUTTONUP:                                  #Si le click est UP

            self.mousePressed = False
            self.lastPos = (0, 0)
            self.dy = 0

            pos = pygame.mouse.get_pos()                                        #Recupere la position du click

            if Helper.clickIsInRect(pos, self.backButton.get_rect(), self.backButtonPos):
                self.gamePanel.changeScene(MainMenuScene.MainMenuScene(self.gamePanel))

        if event.type == pygame.MOUSEBUTTONDOWN:
            self.mousePressed = True

            pos = pygame.mouse.get_pos()

            for ballview in self.ballViews:
                if(Helper.clickIsInRect(pos, ballview.getSelectorRect(), ballview.getSelectorPos())):
                    if(ballview.paid == False):
                        if(Helper.canPayBall(ballview.ball)):
                            Helper.payBall(ballview.ball)
                            self.refreshPaidBalls()
                            self.unselectAllBall()
                            ballview.selected = True
                            Helper.setSelectedBall(ballview.ball.id)
                    else:
                        self.unselectAllBall()
                        ballview.selected = True
                        Helper.setSelectedBall(ballview.ball.id)

    def update(self):

        self.refreshCoinText()

        if self.mousePressed == True:
            pos = pygame.mouse.get_pos()
            if(self.lastPos == (0, 0)):
                self.lastPos = pos

            self.dy = self.lastPos[1] - pos[1]
            self.dy = abs(self.dy)

            for ballview in self.ballViews:
                if(self.lastPos[1] > pos[1]):
                    if(self.ballViews[len(self.ballViews)-1].backgroundPos[1] + self.ballViews[len(self.ballViews)-1].height > self.gamePanel.screenHeight):
                        ballview.move(0, -self.dy)  #DESCENDRE
                else:
                    if(self.ballViews[0].backgroundPos[1] < self.ballViews[0].oriY):
                        ballview.move(0, self.dy)   #MONTER
                    else:
                        ballview.restoreOriginalPos()

            self.lastPos = pos
        for ballview in self.ballViews:
            ballview.update()

    def draw(self, fen):
        fen.fill(Colors.white)

        for ballview in self.ballViews:
            ballview.draw(fen)

        fen.blit(self.backButton, self.backButtonPos)
        fen.blit(self.coinText, self.coinTextPos)
        fen.blit(self.piece, self.piecePos)

    def unselectAllBall(self):
        for ballview in self.ballViews:
            ballview.selected = False

    def refreshCoinText(self):
        self.coinText = self.font.render(Helper.getCoin(), 1, Colors.yellow)
        self.coinTextPos = self.coinText.get_rect()
        self.coinTextPos.x = self.gamePanel.screenWidth/2 - int(self.coinTextPos.width / 2) - 1
        self.piece = pygame.transform.scale(self.piece, (self.coinTextPos.height, self.coinTextPos.height))
        self.piecePos = self.piece.get_rect()
        self.piecePos.x = self.coinTextPos.x + self.coinTextPos.width + 1
        self.piecePos.y = 5
        self.coinTextPos.y = 7

    def refreshPaidBalls(self):
        paidBalls = Helper.getPaidBallsList()
        for i in paidBalls:
            for ballview in self.ballViews:
                if(int(i) == ballview.ball.id):
                    ballview.paid = True