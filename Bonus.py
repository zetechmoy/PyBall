#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

from abc import ABCMeta, abstractmethod

class Bonus(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def doGraphicEffect(self):
        #print("doGraphicEffects")
        pass
    @abstractmethod
    def doScoreEffect(self, score):
        #print("doScoreEffect")
        return score + 1

    @abstractmethod
    def doPlayerEffectOnPlatformCollision(self, player, platform):
        player.dead = True
        #print("doPlayerEffectOnPlatformCollision")

    @abstractmethod
    def doOnCollisionEffect(self, player, platforms):
        #print("doOnCollisionEffect")
        pass
