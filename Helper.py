#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

#Methodes qui servent dans toutes les Scenes du jeu
from abc import ABCMeta, abstractmethod
import pygame, random, sys, os, math, Balls
import ValueManager

from MultiplicationBonus import MultiplicationBonus
from SlowBonus import SlowBonus
from SpeedBonus import SpeedBonus
from ShieldBonus import ShieldBonus

from GameTheme import *

@abstractmethod
def clickIsInRect(clickPos, rect, objPos):                                  #Retourne True si l'utilisateur click dans le rectangle rect
    if(objPos[0] <= clickPos[0] <= objPos[0] + rect[2]) and (objPos[1] <= clickPos[1] <= objPos[1] + rect[3]):
        return True
    return False

@abstractmethod
def collision(rect1,rect2):													#Retourne True si rect1 et rect2 se sont rencontrés
    if rect1.colliderect(rect2):
        return True
    return

@abstractmethod
def surfaceFromRect(rect, color):											#Retourne une Surface de rect colore avec color
    s =  pygame.Surface(rect.size)
    s.set_colorkey(color, pygame.RLEACCEL)
    return s

@abstractmethod
def getRandomBonus(lastBonus):												#Retourne un Bonus parmis ceux crees aleatoirement, si un nouveau bonus est cree, il faut le rajouter a la liste bonus
    bonus = [SlowBonus(), MultiplicationBonus(), SpeedBonus(), ShieldBonus()]
    if(lastBonus != None):
        for i in range(0, len(bonus)):
            if (lastBonus.id == bonus[i].id):
                bonus.pop(i)
                break

    return bonus[random.randint(0, len(bonus)-1)]

@abstractmethod
def addCoin(coin):															#Ajoute 1 a la somme d'argent
    coins = int(ValueManager.get("coins", "0"))
    coins += coin
    ValueManager.save("coins", coins)

@abstractmethod
def getCoin():																#Retourne la somme d'argent
    return ValueManager.get("coins", "0")

@abstractmethod
def surfaceFromRect(r, color):												#Retourne une Surface de rect colore avec color
    rect = pygame.Rect(r)
    s = pygame.Surface(rect.size)
    s.fill(color)
    return s

@abstractmethod
def getRandomTheme(lastTheme):												#Retourne un Theme parmis ceux crees aleatoirement, si un nouveau bonus est cree, il faut le rajouter a la liste themes
    themes = [RedGameTheme(), BlueGameTheme(), Blue2GameTheme(), GreenGameTheme(), PinkGameTheme()]
    if (lastTheme != None):
        for i in range(0, len(themes)):
            if (lastTheme.id == themes[i].id):
                themes.pop(i)
                break
    return themes[random.randint(0, len(themes) - 1)]

@abstractmethod
def degreesToRadians(deg):													#Retourne un angle en radian
    return deg/180.0 * math.pi

@abstractmethod
def drawCircleArc(screen,color,center,radius,startDeg,endDeg,thickness):	#Dessine un arc de cercle sur screen
    (x,y) = center
    rect = (x-radius,y-radius,radius*2,radius*2)
    startRad = degreesToRadians(startDeg)
    endRad = degreesToRadians(endDeg)

    pygame.draw.arc(screen,color,rect,startRad,endRad,thickness)

@abstractmethod
def setSelectedBall(which):													#Selectionnne une balle
    ValueManager.save("selectedBall", str(which))

@abstractmethod
def getSelectedBall():														#Retourne la balle selectionnee
    return ValueManager.get("selectedBall", "0")

@abstractmethod
def getPaidBalls():															#Retourne les balles payes (avec l'argent du jeu) sous la forme 0-1-2-3...
    return ValueManager.get("paidBalls", "0")

@abstractmethod
def getPaidBallsList():														#Retourne la liste de balles payes
    return ValueManager.get("paidBalls", "0").split("-")

@abstractmethod
def setPaidBalls(paidBalls):												#Modifie les balles payes
    ValueManager.save("paidBalls", paidBalls)

@abstractmethod
def canPayBall(ball):														#Retourne True si une balles peut etre acheter
    coins = int(ValueManager.get("coins", "0"))
    if(ball.price <= coins):
        return True
    return False

@abstractmethod
def payBall(ball):															#Achete une balle
    coins = int(ValueManager.get("coins", "0"))
    coins -= ball.price
    ValueManager.save("coins", str(coins))
    setPaidBalls(getPaidBalls()+"-"+str(ball.id))