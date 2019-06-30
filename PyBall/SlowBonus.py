#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

from Bonus import Bonus

class SlowBonus(Bonus):

    def __init__(self):
        self.bonusDuration = 5#s
        self.name = "SlowBonus !"
        self.timeBetween2Platform = 5#s
        self.id = 1

    def doOnCollisionEffect(self, player, platforms):
        player.slow = True

