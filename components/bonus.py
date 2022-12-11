# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------

from abc import ABC, abstractmethod


class Bonus(ABC):

    bonusDuration = 3  # s
    name = "Bonus"
    timeBetween2Platform = 1  # s
    id = -1

    @abstractmethod
    def doGraphicEffect(self):
        pass

    @abstractmethod
    def doScoreEffect(self, score):
        return score + 1

    @abstractmethod
    def doPlayerEffectOnPlatformCollision(self, player, platform):
        player.dead = True

    @abstractmethod
    def doOnCollisionEffect(self, player, platforms):
        pass


class ShieldBonus(Bonus):
    def __init__(self):
        self.bonusDuration = 0  # s
        self.name = "ShieldBonus !"
        self.timeBetween2Platform = 2.5  # s
        self.id = 3

    def doOnCollisionEffect(self, player, platforms):
        player.shield = True


class SlowBonus(Bonus):
    def __init__(self):
        self.bonusDuration = 5  # s
        self.name = "SlowBonus !"
        self.timeBetween2Platform = 5  # s
        self.id = 1

    def doOnCollisionEffect(self, player, platforms):
        player.slow = True


class SpeedBonus(Bonus):
    def __init__(self):
        self.bonusDuration = 5  # s
        self.name = "SpeedBonus !"
        self.timeBetween2Platform = 0.300  # s
        self.id = 2

    def doOnCollisionEffect(self, player, platforms):
        player.speed = True


class MultiplicationBonus(Bonus):
    def __init__(self):
        self.bonusDuration = 5  # s
        self.name = "Scorex2 !"
        self.timeBetween2Platform = 1.5  # s
        self.id = 0

    def doScoreEffect(self, score):
        return score + 2
