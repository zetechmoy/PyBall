import components.colors as colors
from components.theme import Theme


class BlueGameTheme(Theme):
    def __init__(self):
        self.backgroundColor = colors.blue_theme_background
        self.ballColor = colors.blue_theme_ball
        self.platformColor = colors.blue_theme_platform
        self.scoreColor = colors.blue_theme_score
        self.effectColor = colors.blue_theme_platform
        self.platform = "square_blue.png"
        self.bonus = "circle_blue.png"
        self.id = 2
