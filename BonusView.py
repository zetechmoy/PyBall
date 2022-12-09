#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

import random, pygame, Constants, Helper, Colors

class BonusView:

    def __init__(self, gamescene, gamepanel):
        pygame.init()
        self.width = 40
        self.height = self.width
        self.gameScene = gamescene
        self.gamePanel = gamepanel
        self.x = self.gamePanel.screenWidth + 100
        self.y = random.randint(0, 600-self.height)
        self.fast = Constants.screenWidth / 5 / Constants.FPS #2.5 -> 60FPS/5 -> 30FPS
        self.img = pygame.image.load('./drawable/'+self.gameScene.getCurrentTheme().bonus).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.width, self.height))

        self.currentCircleColor = self.gameScene.getCurrentTheme().bonus

        self.collisionned = False
        self.isABonus = False
        self.bonusGiven = False
        self.coinGiven = False

        if(random.randint(0, 4) == 2):#NE PAS FAIRE UN BONUS A CHAQUE COLLISION => random.randint(0, 4) == 2
            self.isABonus = True;
            self.shadow = pygame.image.load('./drawable/square_shadow.png')
        else:
            self.shadow = pygame.image.load('./drawable/ball_shadow.png')

        self.shadow = pygame.transform.scale(self.shadow, (self.width, self.height))


    def update(self):
        self.x = self.x - self.fast
        #print("bonusview.x :", self.x)
        if(self.gameScene.getCurrentTheme().bonus != self.currentCircleColor):
            self.img = pygame.image.load('./drawable/'+self.gameScene.getCurrentTheme().bonus).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.width, self.height))


    def draw(self, fenetre):
        if(self.coinGiven == False):
            if self.isABonus == True:
                fenetre.blit(self.shadow, (self.x + self.width/12, self.y + self.height/12))
                rect = Helper.surfaceFromRect(pygame.Rect(self.x, self.y, self.width, self.height), self.gameScene.getCurrentTheme().ballColor)
                fenetre.blit(rect, (self.x, self.y))
            else:
                fenetre.blit(self.shadow, (self.x + self.width/12, self.y + self.height/12))
                fenetre.blit(self.img, (self.x, self.y))

    def centerX(self):
        return self.x + self.width/2

    def centerY(self):
        return self.y + self.height/2

    def X(self):
        return self.x

    def Y(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def getRect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def getRectSurface(self):
        rect = pygame.Rect(self.x, self.y, self.width, self.height)
        s = pygame.Surface(rect.size)
        s.set_colorkey((68,132,235), pygame.RLEACCEL)
        return s