# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------

# Methodes qui servent dans toutes les Scenes du jeu
from abc import ABCMeta, abstractmethod
import pygame, random, sys, os, math, components.ball as ball
from components.value_manager import ValueManager
import Constants

from components.bonus import MultiplicationBonus
from components.bonus import SlowBonus
from components.bonus import SpeedBonus
from components.bonus import ShieldBonus

from themes.blue import BlueGameTheme
from themes.blue2 import Blue2GameTheme
from themes.red import RedGameTheme
from themes.green import GreenGameTheme
from themes.pink import PinkGameTheme

from balls.boomerang import BoomerangBall
from balls.chrome import ChromeBall
from balls.cool import CoolBall
from balls.croit import CroitBall
from balls.default import DefaultBall
from balls.ellipse import EllipseBall
from balls.happy import HappyBall
from balls.helice import HeliceBall
from balls.radioactif import RadioactifBall
from balls.star import StarBall
from balls.super import SuperBall
from balls.tennis import TennisBall
from balls.time import TimeBall
from balls.ubi import UbiBall
from balls.youtube import YoutubeBall


@abstractmethod
def clickIsInRect(
    clickPos, rect, objPos
):  # Retourne True si l'utilisateur click dans le rectangle rect
    if (objPos[0] <= clickPos[0] <= objPos[0] + rect[2]) and (
        objPos[1] <= clickPos[1] <= objPos[1] + rect[3]
    ):
        return True
    return False


@abstractmethod
def getPointAtAngle(x, y, angle, distance):
    return (
        x + distance * math.cos(math.radians(angle)),
        y + distance * math.sin(math.radians(angle)),
    )


@abstractmethod
def getDistance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


@abstractmethod
def getNormalisedDistance(x1, y1, x2, y2):
    y1 = y1 / Constants.screenHeight
    y2 = y2 / Constants.screenHeight

    x1 = x1 / Constants.screenWidth
    x2 = x2 / Constants.screenWidth

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


@abstractmethod
def isInLine(
    x, y, angle, x2, y2, w2, h2
):  # Retourne True si le point (x,y) est dans la ligne de l'angle angle et de la position x2,y2 et de la taille w2,h2
    if angle == 90:
        if (x2 - w2 / 2 <= x <= x2 + w2 / 2) and (y2 <= y <= y2 + h2):
            return True
        return False
    elif angle == 270:
        if (x2 - w2 / 2 <= x <= x2 + w2 / 2) and (y2 - h2 <= y <= y2):
            return True
        return False
    elif angle == 0:
        if (x2 <= x <= x2 + w2) and (y2 - h2 / 2 <= y <= y2 + h2 / 2):
            return True
        return False
    elif angle == 180:
        if (x2 - w2 <= x <= x2) and (y2 - h2 / 2 <= y <= y2 + h2 / 2):
            return True
        return False

    a = math.tan(math.radians(angle))
    b = y2 - a * x2
    if (x2 <= x <= x2 + w2) and (y == a * x + b):
        return True
    return False


@abstractmethod
def getIntersections(
    lineFrom, lineTo, x, y, w, h
):  # Retourne le point d'intersection entre la ligne et le rectangle

    P0 = lineFrom
    P1 = lineTo
    Q0left = (x, y)
    Q1left = (x, y + h)

    Q0right = (x + w, y)
    Q1right = (x + w, y + h)

    Q0top = (x, y)
    Q1top = (x + w, y)

    Q0bottom = (x, y + h)
    Q1bottom = (x + w, y + h)

    left = lineLineIntersect(P0, P1, Q0left, Q1left)
    right = lineLineIntersect(P0, P1, Q0right, Q1right)
    top = lineLineIntersect(P0, P1, Q0top, Q1top)
    bottom = lineLineIntersect(P0, P1, Q0bottom, Q1bottom)

    return [x for x in [left, right, top, bottom] if x]


@abstractmethod
def lineLineIntersect(P0, P1, Q0, Q1):
    d = (P1[0] - P0[0]) * (Q1[1] - Q0[1]) + (P1[1] - P0[1]) * (Q0[0] - Q1[0])
    if d == 0:
        return None
    t = ((Q0[0] - P0[0]) * (Q1[1] - Q0[1]) + (Q0[1] - P0[1]) * (Q0[0] - Q1[0])) / d
    u = ((Q0[0] - P0[0]) * (P1[1] - P0[1]) + (Q0[1] - P0[1]) * (P0[0] - P1[0])) / d
    if 0 <= t <= 1 and 0 <= u <= 1:
        return round(P1[0] * t + P0[0] * (1 - t)), round(P1[1] * t + P0[1] * (1 - t))
    return None


@abstractmethod
def collision(rect1, rect2):  # Retourne True si rect1 et rect2 se sont rencontrés
    if rect1.colliderect(rect2):
        return True
    return


@abstractmethod
def surfaceFromRect(rect, color):  # Retourne une Surface de rect colore avec color
    s = pygame.Surface(rect.size)
    s.set_colorkey(color, pygame.RLEACCEL)
    return s


@abstractmethod
def getRandomBonus(
    lastBonus,
):  # Retourne un Bonus parmis ceux crees aleatoirement, si un nouveau bonus est cree, il faut le rajouter a la liste bonus
    bonus = [SlowBonus(), MultiplicationBonus(), SpeedBonus(), ShieldBonus()]
    if lastBonus != None:
        for i in range(0, len(bonus)):
            if lastBonus.id == bonus[i].id:
                bonus.pop(i)
                break

    return bonus[random.randint(0, len(bonus) - 1)]


@abstractmethod
def addCoin(coin):  # Ajoute 1 a la somme d'argent
    coins = int(ValueManager.get("coins", "0"))
    coins += coin
    ValueManager.save("coins", coins)


@abstractmethod
def getCoin():  # Retourne la somme d'argent
    return ValueManager.get("coins", "0")


@abstractmethod
def surfaceFromRect(r, color):  # Retourne une Surface de rect colore avec color
    rect = pygame.Rect(r)
    s = pygame.Surface(rect.size)
    s.fill(color)
    return s


@abstractmethod
def getRandomTheme(
    lastTheme,
):  # Retourne un Theme parmis ceux crees aleatoirement, si un nouveau bonus est cree, il faut le rajouter a la liste themes
    themes = [
        RedGameTheme(),
        BlueGameTheme(),
        Blue2GameTheme(),
        GreenGameTheme(),
        PinkGameTheme(),
    ]
    if lastTheme != None:
        for i in range(0, len(themes)):
            if lastTheme.id == themes[i].id:
                themes.pop(i)
                break
    return themes[random.randint(0, len(themes) - 1)]


@abstractmethod
def getThemeById(id):
    themes = [
        RedGameTheme(),
        BlueGameTheme(),
        Blue2GameTheme(),
        GreenGameTheme(),
        PinkGameTheme(),
    ]
    for i in range(0, len(themes)):
        if id == themes[i].id:
            return themes[i]


@abstractmethod
def degreesToRadians(deg):  # Retourne un angle en radian
    return deg / 180.0 * math.pi


@abstractmethod
def drawCircleArc(
    screen, color, center, radius, startDeg, endDeg, thickness
):  # Dessine un arc de cercle sur screen
    (x, y) = center
    rect = (x - radius, y - radius, radius * 2, radius * 2)
    startRad = degreesToRadians(startDeg)
    endRad = degreesToRadians(endDeg)

    pygame.draw.arc(screen, color, rect, startRad, endRad, thickness)


@abstractmethod
def setSelectedBall(which):  # Selectionnne une balle
    ValueManager.save("selectedBall", str(which))


@abstractmethod
def getSelectedBall():  # Retourne la balle selectionnee
    return ValueManager.get("selectedBall", "0")


@abstractmethod
def getPaidBalls():  # Retourne les balles payes (avec l'argent du jeu) sous la forme 0-1-2-3...
    return ValueManager.get("paidBalls", "0")


@abstractmethod
def getPaidBallsList():  # Retourne la liste de balles payes
    return ValueManager.get("paidBalls", "0").split("-")


@abstractmethod
def setPaidBalls(paidBalls):  # Modifie les balles payes
    ValueManager.save("paidBalls", paidBalls)


@abstractmethod
def canPayBall(ball):  # Retourne True si une balles peut etre acheter
    coins = int(ValueManager.get("coins", "0"))
    if ball.price <= coins:
        return True
    return False


@abstractmethod
def payBall(ball):  # Achete une balle
    coins = int(ValueManager.get("coins", "0"))
    coins -= ball.price
    ValueManager.save("coins", str(coins))
    setPaidBalls(getPaidBalls() + "-" + str(ball.id))


@abstractmethod
def getBalls():  # Retourne une liste de balles, il faut la rajouter a la liste si vous voulez qu'elle soit affichee
    t = [
        DefaultBall(),
        CroitBall(),
        BoomerangBall(),
        ChromeBall(),
        CoolBall(),
        EllipseBall(),
        HappyBall(),
        HeliceBall(),
        RadioactifBall(),
        StarBall(),
        SuperBall(),
        TennisBall(),
        TimeBall(),
        UbiBall(),
        YoutubeBall(),
    ]
    return t
