import components.colors as colors
from components.theme import Theme


class RedGameTheme(Theme):
    def __init__(self):
        self.backgroundColor = colors.red_theme_background
        self.ballColor = colors.red_theme_ball
        self.platformColor = colors.red_theme_platform
        self.scoreColor = colors.red_theme_score
        self.effectColor = colors.red_theme_platform
        self.platform = "square_red.png"
        self.bonus = "circle_red.png"
        self.id = 1
