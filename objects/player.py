# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------
import os, random
import pygame, math, uuid
from pygame.locals import *

import components.helper as helper
from components.animation import Animation
import Constants

import components.colors as colors

from components.ball import *
from components.object import Object
from components.player_controller import PlayerController


class Player(Object):
    def __init__(self, controller: PlayerController, posX, posY, w, h):
        self.id = uuid.uuid4()
        self.width = w  # Largeur du joueur
        self.height = h  # Hauteur du joueur
        self.FPS = Constants.FPS
        self.fast = (
            Constants.screenHeight / 40 / Constants.FPS
        )  # 0.25 -> 60FPS/0.5 -> 30FPS          #De combien on bouge de pixel entre chaque update
        self.movingUp = False
        self.isPlaying = False
        self.dy = 0
        self.maxDy = 40 / (Constants.FPS / 15)
        self.lastPos = []
        self.pointSpeed = int((math.sqrt(Constants.screenWidth) / 4))
        self.maxPoint = 10
        self.dead = False

        self.ball = helper.getBalls()[int(helper.getSelectedBall())]

        self.theme = Constants.initTheme

        self.shadow = pygame.image.load("./drawable/ball_shadow.png")
        self.shadow = pygame.transform.scale(self.shadow, (self.width, self.height))

        self.currentSpritesheet = self.ball.yellow_spritesheet

        self.animation = Animation(
            self.currentSpritesheet, 50, 50, self.ball.numFrames, self.ball.speed
        )

        self.pos = pygame.Rect(0, 0, 0, 0)

        self.pos.x = posX
        self.pos.y = posY

        # BONUS
        self.slow = False
        self.shield = False
        self.speed = False

        self.controller = controller
        self.isPlaying = True

        createEvent = pygame.event.Event(
            Constants.PLAYER_CREATED_EVENT,
            {
                "id": self.id,
                "x": self.pos.x,
                "y": self.pos.y,
                "width": self.width,
                "height": self.height,
                "isPlaying": self.isPlaying,
                # "score": self.score,
            },
        )
        pygame.event.post(createEvent)

    def spriteSheetFromTheme(self, theme):
        if theme.id == 0:
            return self.ball.yellow_spritesheet
        elif theme.id == 1:
            return self.ball.red_spritesheet
        elif theme.id == 2:
            return self.ball.blue_spritesheet
        elif theme.id == 3:
            return self.ball.blue2_spritesheet
        elif theme.id == 4:
            return self.ball.green_spritesheet
        elif theme.id == 5:
            return self.ball.pink_spritesheet

    def newSpritesheet(self):
        self.animation.setSpritesheet(self.img)

    def onEvent(self, event):
        # En utilisant la barre d'espace
        ##        if event.type == KEYDOWN:
        ##            if event.key == K_SPACE:
        ##                if self.isPlaying == False:
        ##                    self.isPlaying = True
        ##                else:
        ##                    self.movingUp = True
        ##        if event.type == KEYUP:
        ##            if event.key == K_SPACE:
        ##                self.movingUp = False

        # En utilisant la souris
        ##        if event.type == pygame.MOUSEBUTTONUP:
        ##            pos = pygame.mouse.get_pos()
        ##            self.movingUp = False
        ##        if event.type == pygame.MOUSEBUTTONDOWN:
        ##            if self.isPlaying == False:
        ##                self.isPlaying = True
        ##            else:
        ##                self.movingUp = True
        if event.type == Constants.NEW_GAME_THEME_EVENT:
            data = event.__dict__
            newThemeId = data["id"]
            theme = helper.getThemeById(newThemeId)
            self.currentSpritesheet = self.spriteSheetFromTheme(theme)
            self.animation.setSpritesheet(self.currentSpritesheet)

        self.controller.onEvent(event)
        self.controller.onEventWithPlayer(event, self)

    def update(self):

        self.animation.update()

        if self.isPlaying == True:

            if self.movingUp == False:
                self.dy = self.dy + self.fast
            else:
                self.dy = self.dy - self.fast

            if self.dy > self.maxDy:
                self.dy = self.maxDy  # Recalcule maxDy et minDy en fonction des FPS
            if self.dy < -self.maxDy:
                self.dy = -self.maxDy

            if self.slow == True:
                self.pos.y += self.dy
            else:
                self.pos.y += 3 * self.dy

            moveEvent = pygame.event.Event(
                Constants.PLAYER_MOVE_EVENT,
                {
                    "id": self.id,
                    "x": self.pos.x,
                    "y": self.pos.y,
                    "width": self.width,
                    "height": self.height,
                    "isPlaying": self.isPlaying,
                    # "score": self.score,
                },
            )
            pygame.event.post(moveEvent)

            self.lastPos.append((self.pos.x, self.pos.y))

            if len(self.lastPos) > self.maxPoint:
                self.lastPos.pop(0)

            for i in range(0, len(self.lastPos)):
                self.lastPos[i] = (
                    self.lastPos[i][0] - self.pointSpeed,
                    self.lastPos[i][1],
                )

    def draw(self, fenetre):
        if self.isPlaying == True:
            self.movingUp = self.controller.decideUpOrDown()
            for i in range(0, len(self.lastPos)):
                radius = int((self.width / 4 / (((self.maxPoint + 1) - i) / 3)))
                pygame.draw.circle(
                    fenetre,
                    self.theme.effectColor,
                    (
                        self.lastPos[i][0] + int(self.width / 2),
                        self.lastPos[i][1] + int(self.height / 2),
                    ),
                    radius,
                )
        fenetre.blit(
            self.shadow, (self.pos.x + self.width / 12, self.pos.y + self.height / 12)
        )
        fenetre.blit(self.animation.getImage(), self.pos)
        if self.shield == True:
            helper.drawCircleArc(
                fenetre,
                self.theme.ballColor,
                (
                    int(self.pos.x + self.width / 2 + 8),
                    int(self.pos.y + self.height / 2),
                ),
                int(self.width / 2 + 2),
                -70,
                70,
                5,
            )

    def centerX(self):
        return self.pos.x + self.width / 2

    def centerY(self):
        return self.pos.y + self.height / 2

    def X(self):
        return self.pos.x

    def Y(self):
        return self.pos.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getRect(self):
        return pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)

    def getRectSurface(self):
        rect = Rect(self.x, self.y, self.width, self.height)
        s = pygame.Surface(rect.size)
        s.set_colorkey((68, 132, 235), pygame.RLEACCEL)
        return s

    def getAnimation(self):
        return self.animation

    def destroy(self):
        # self.score = self.score - 15
        destroyEvent = pygame.event.Event(
            Constants.PLAYER_DELETE_EVENT,
            {
                "id": self.id,
                "x": self.pos.x,
                "y": self.pos.y,
                "width": self.width,
                "height": self.height,
                "isPlaying": self.isPlaying,
                # "score": self.score,
            },
        )
        pygame.event.post(destroyEvent)
