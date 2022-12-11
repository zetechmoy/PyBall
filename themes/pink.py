import components.colors as colors
from components.theme import Theme


class PinkGameTheme(Theme):
    def __init__(self):
        self.backgroundColor = colors.pink_theme_background
        self.ballColor = colors.pink_theme_ball
        self.platformColor = colors.pink_theme_platform
        self.scoreColor = colors.pink_theme_score
        self.effectColor = colors.pink_theme_platform
        self.platform = "square_pink.png"
        self.bonus = "circle_pink.png"
        self.id = 5
