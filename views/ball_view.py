# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------

import pygame
import components.helper as helper
import components.colors as colors
import operator


class BallView:
    def __init__(self, gmp, ball, x, y):

        pygame.init()

        self.gamePanel = gmp

        self.ball = ball
        self.space = 6

        self.width, self.height = (
            self.gamePanel.screenWidth / 2,
            self.gamePanel.screenHeight / 4,
        )

        self.ballHeight = self.ballWidth = int((self.height - 4 * self.space) / 2)

        self.backgroundRect = pygame.Rect(
            0, 0, int(self.width - 2 * self.space), int(self.height - 2 * self.space)
        )
        self.backgroundSurface = helper.surfaceFromRect(
            self.backgroundRect, colors.deep_purple
        )
        self.backgroundPos = (x + self.space, y + self.space)

        self.oriX = x + self.space
        self.oriY = y + self.space

        self.ballSpritesheet = pygame.image.load(
            "./drawable/" + self.ball.yellow_spritesheet
        )
        self.ballPreview = self.image_at(pygame.Rect(0, 0, 100, 100))
        self.ballPreview = pygame.transform.scale(
            self.ballPreview, (self.ballWidth, self.ballHeight)
        )
        self.ballPos = (
            self.backgroundPos[0] + self.width / 4 - self.ballWidth / 2,
            self.backgroundPos[1] + self.height / 2 - self.ballHeight / 2 - self.space,
        )

        self.shadow = pygame.image.load("./drawable/ball_shadow.png")
        self.shadow = pygame.transform.scale(
            self.shadow,
            (self.ballWidth + 2 * self.space, self.ballHeight + 2 * self.space),
        )
        self.shadowPos = (
            self.backgroundPos[0]
            + self.width / 4
            - (self.ballWidth + 2 * self.space) / 2,
            self.backgroundPos[1]
            + self.height / 2
            - (self.ballHeight + 2 * self.space) / 2
            - self.space,
        )

        self.font = pygame.font.Font("./fonts/Hero.otf", 25)

        self.ballTitle = self.font.render(self.ball.name, 1, colors.white)
        self.ballTitlePos = self.ballTitle.get_rect()
        self.ballTitlePos.centerx = self.backgroundPos[0] + self.width / 2
        self.ballTitlePos.y = (
            self.backgroundPos[1] + self.height / 2 - self.ballTitlePos[3]
        )

        self.ballPrice = self.font.render(str(self.ball.price) + "p.", 1, colors.white)
        self.ballPricePos = self.ballPrice.get_rect()
        self.ballPricePos.centerx = self.backgroundPos[0] + self.width / 2
        self.ballPricePos.y = self.ballTitlePos.y + self.ballTitlePos.height

        self.selectorRadius = int(self.height / 5)
        self.selectorPos = (
            int(self.backgroundPos[0] + (self.width / 4 * 3)),
            int(self.backgroundPos[1] + self.height / 2),
        )
        self.selectorRect = None

        self.selected = False
        self.paid = False

    def onEvent(self, event):
        pass

    def update(self):
        self.ballPos = (
            self.backgroundPos[0] + self.width / 4 - self.ballWidth / 2,
            self.backgroundPos[1] + self.height / 2 - self.ballHeight / 2 - self.space,
        )
        self.shadowPos = (
            self.backgroundPos[0]
            + self.width / 4
            - (self.ballWidth + 2 * self.space) / 2,
            self.backgroundPos[1]
            + self.height / 2
            - (self.ballHeight + 2 * self.space) / 2
            - self.space,
        )
        self.selectorPos = (
            int(self.backgroundPos[0] + (self.width / 4 * 3)),
            int(self.backgroundPos[1] + self.height / 2),
        )

        self.updateTextPos()

    def draw(self, fen):
        fen.blit(self.backgroundSurface, self.backgroundPos)
        fen.blit(self.shadow, self.shadowPos)
        fen.blit(self.ballPreview, self.ballPos)
        fen.blit(self.ballTitle, self.ballTitlePos)
        fen.blit(self.ballPrice, self.ballPricePos)

        self.selectorRect = pygame.draw.circle(
            fen, colors.yellow, self.selectorPos, self.selectorRadius
        )

        if self.paid == True:
            if self.selected == True:
                pygame.draw.circle(
                    fen, colors.green, self.selectorPos, int(self.selectorRadius / 2)
                )
            else:
                pygame.draw.circle(
                    fen, colors.yellow, self.selectorPos, int(self.selectorRadius / 2)
                )
        else:
            pygame.draw.circle(
                fen, colors.red, self.selectorPos, int(self.selectorRadius / 2)
            )

    def move(self, dx, dy):
        self.backgroundPos = (self.backgroundPos[0] + dx, self.backgroundPos[1] + dy)

    def restoreOriginalPos(self):
        self.backgroundPos = (self.oriX, self.oriY)

    def updateTextPos(self):
        self.ballTitlePos = self.ballTitle.get_rect()
        self.ballTitlePos.centerx = self.backgroundPos[0] + self.width / 2
        self.ballTitlePos.y = (
            self.backgroundPos[1] + self.height / 2 - self.ballTitlePos[3]
        )

        self.ballPricePos = self.ballPrice.get_rect()
        self.ballPricePos.centerx = self.backgroundPos[0] + self.width / 2
        self.ballPricePos.y = self.ballTitlePos.y + self.ballTitlePos.height

    def image_at(self, rectangle, colorkey=None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size, pygame.SRCALPHA, 32)
        image.blit(self.ballSpritesheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    def getSelectorRect(self):
        return self.selectorRect

    def getSelectorPos(self):
        # tuple(map(operator.add/sub, tup1, tup2)) to math with tuple like (1,2,3) + (3,2,1) = (4,4,4)
        return tuple(
            map(
                operator.sub,
                self.selectorPos,
                (self.selectorRadius, self.selectorRadius),
            )
        )
