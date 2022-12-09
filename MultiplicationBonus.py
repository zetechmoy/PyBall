#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------

from Bonus import Bonus

class MultiplicationBonus(Bonus):

    def __init__(self):
        self.bonusDuration = 5#s
        self.name = "Scorex2 !"
        self.timeBetween2Platform = 1.5#s
        self.id = 0

    def doScoreEffect(self, score):
        return score + 2
