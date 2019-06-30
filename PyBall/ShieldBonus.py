#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------
from Bonus import Bonus

class ShieldBonus(Bonus):
    def __init__(self):
        self.bonusDuration = 0#s
        self.name = "ShieldBonus !"
        self.timeBetween2Platform = 2.5#s
        self.id = 3

    def doOnCollisionEffect(self, player, platforms):
        player.shield = True