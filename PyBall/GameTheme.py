#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------
import Colors

class YellowGameTheme():
    def __init__(self):
        self.backgroundColor = Colors.white
        self.ballColor = Colors.yellow
        self.platformColor = Colors.deep_purple
        self.scoreColor = Colors.grey_overlay
        self.effectColor = Colors.yellow
        self.platform = "square_yellow.png"
        self.bonus = "circle_yellow.png"
        self.id = 0

class RedGameTheme():
    def __init__(self):
        self.backgroundColor = Colors.red_theme_background
        self.ballColor = Colors.red_theme_ball
        self.platformColor = Colors.red_theme_platform
        self.scoreColor = Colors.red_theme_score
        self.effectColor = Colors.red_theme_platform
        self.platform = "square_red.png"
        self.bonus = "circle_red.png"
        self.id = 1

class BlueGameTheme():
    def __init__(self):
        self.backgroundColor = Colors.blue_theme_background
        self.ballColor = Colors.blue_theme_ball
        self.platformColor = Colors.blue_theme_platform
        self.scoreColor = Colors.blue_theme_score
        self.effectColor = Colors.blue_theme_platform
        self.platform = "square_blue.png"
        self.bonus = "circle_blue.png"
        self.id = 2

class Blue2GameTheme():
    def __init__(self):
        self.backgroundColor = Colors.blue2_theme_background
        self.ballColor = Colors.blue2_theme_ball
        self.platformColor = Colors.blue2_theme_platform
        self.scoreColor = Colors.blue2_theme_score
        self.effectColor = Colors.blue2_theme_platform
        self.platform = "square_blue2.png"
        self.bonus = "circle_blue2.png"
        self.id = 3

class GreenGameTheme():
    def __init__(self):
        self.backgroundColor = Colors.green_theme_background
        self.ballColor = Colors.green_theme_ball
        self.platformColor = Colors.green_theme_platform
        self.scoreColor = Colors.green_theme_score
        self.effectColor = Colors.green_theme_platform
        self.platform = "square_green.png"
        self.bonus = "circle_green.png"
        self.id = 4

class PinkGameTheme():
    def __init__(self):
        self.backgroundColor = Colors.pink_theme_background
        self.ballColor = Colors.pink_theme_ball
        self.platformColor = Colors.pink_theme_platform
        self.scoreColor = Colors.pink_theme_score
        self.effectColor = Colors.pink_theme_platform
        self.platform = "square_pink.png"
        self.bonus = "circle_pink.png"
        self.id = 5

