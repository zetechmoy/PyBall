#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

from Bonus import Bonus

class SpeedBonus(Bonus):

    def __init__(self):
        self.bonusDuration = 5#s
        self.name = "SpeedBonus !"
        self.timeBetween2Platform = 0.300#s
        self.id = 2

    def doOnCollisionEffect(self, player, platforms):
        player.speed = True
