#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

import random, pygame, Constants, Helper

class Platform:

	#Cube de couleur que le joueur doit eviter

    def __init__(self, yMin, yMax, gms, gmp):
        pygame.init()
        self.gameScene = gms
        self.gamePanel = gmp
        self.width = random.randint(75, 100)*2
        self.height = self.width
        self.x = self.gamePanel.screenWidth + 100
        self.y = random.randint(yMin, yMax-self.height)
        self.fast = Constants.screenWidth / 4 / Constants.FPS #taille de l'ecran /  temps a l'ecran en s / nb de frames par secondes
        self.img = pygame.image.load('./drawable/'+self.gameScene.getCurrentTheme().platform).convert_alpha()
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.shadow = pygame.image.load('./drawable/square_shadow.png')
        self.shadow = pygame.transform.scale(self.shadow, (self.width, self.height))
        self.collisionned = False

        self.currentPlatformColor = self.gameScene.getCurrentTheme().platform


    def update(self):
        self.x = self.x - self.fast
        if self.gameScene.getCurrentTheme().platform != self.currentPlatformColor:
            self.img = pygame.image.load('./drawable/'+self.gameScene.getCurrentTheme().platform).convert_alpha()
            self.img = pygame.transform.scale(self.img, (self.width, self.height))
        #print("platform.x :",self.x)


    def draw(self, fenetre):
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
