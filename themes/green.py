import components.colors as colors
from components.theme import Theme


class GreenGameTheme(Theme):
    def __init__(self):
        self.backgroundColor = colors.green_theme_background
        self.ballColor = colors.green_theme_ball
        self.platformColor = colors.green_theme_platform
        self.scoreColor = colors.green_theme_score
        self.effectColor = colors.green_theme_platform
        self.platform = "square_green.png"
        self.bonus = "circle_green.png"
        self.id = 4
