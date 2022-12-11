import components.colors as colors
from components.theme import Theme


class Blue2GameTheme(Theme):
    def __init__(self):
        self.backgroundColor = colors.blue2_theme_background
        self.ballColor = colors.blue2_theme_ball
        self.platformColor = colors.blue2_theme_platform
        self.scoreColor = colors.blue2_theme_score
        self.effectColor = colors.blue2_theme_platform
        self.platform = "square_blue2.png"
        self.bonus = "circle_blue2.png"
        self.id = 3
