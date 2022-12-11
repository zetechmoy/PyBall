# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------

from abc import ABC
import components.colors as colors


class Theme(ABC):

    backgroundColor = colors.white
    ballColor = colors.yellow
    platformColor = colors.deep_purple
    scoreColor = colors.grey_overlay
    effectColor = colors.yellow
    platform = "square_yellow.png"
    bonus = "circle_yellow.png"
    id = 0
