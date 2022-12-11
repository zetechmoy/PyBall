# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------

import time
from pygame import Rect
import pygame

import components.helper as helper
from components.object import Object


class Animation(Object):

    # Permet de gerer plus simplement l'affichage de la balle, pour les affichages successifs des sprites

    def __init__(self, spImg, w, h, nbFrames, sp):

        pygame.init()

        self.frames = []
        self.nbFrames = nbFrames
        self.speed = sp
        self.width = w
        self.height = h
        self.currentFrame = 0
        self.millisTime = time.time()
        self.width = w
        self.height = h

        self.spritesheet = pygame.image.load("./drawable/" + spImg)
        # print("animation spritesheetpath : ", './drawable/{}'.format(ball.yellow_spritesheet))
        self.spritesheet = pygame.transform.scale(
            self.spritesheet,
            (
                int(self.spritesheet.get_rect().width / 2),
                int(self.spritesheet.get_rect().height / 2),
            ),
        )

        x, y = 0, 0
        for i in range(0, self.nbFrames):
            # print("cutting here : i = ",i, " -> ", Rect(i * w, 0, w, h))
            self.frames.append(self.image_at(Rect(i * w, 0, w, h)))

    def update(self):
        if float((time.time() - self.millisTime)) >= self.speed:
            self.currentFrame = self.currentFrame + 1
            self.millisTime = time.time()
            if self.currentFrame == len(self.frames):
                self.currentFrame = 0

        # print("currentFrame : ", self.currentFrame)
        super(Animation, self).update()

    def getImage(self):
        return self.frames[self.currentFrame]

    def getSpritesheet(self):
        return self.spritesheet

    def getFrames(self):
        return self.frames

    def setSpritesheet(self, spImg):
        self.spritesheet = pygame.image.load("./drawable/" + spImg)
        # print("animation spritesheetpath : ", './drawable/{}'.format(ball.yellow_spritesheet))
        self.spritesheet = pygame.transform.scale(
            self.spritesheet,
            (
                int(self.spritesheet.get_rect().width / 2),
                int(self.spritesheet.get_rect().height / 2),
            ),
        )
        self.frames.clear()
        for i in range(0, self.nbFrames):
            self.frames.append(
                self.image_at(Rect(i * self.width, 0, self.width, self.height))
            )

    def image_at(self, rectangle, colorkey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        image.blit(self.spritesheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
