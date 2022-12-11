import components.colors as colors
from components.theme import Theme


class YellowGameTheme(Theme):
    def __init__(self):
        self.backgroundColor = colors.white
        self.ballColor = colors.yellow
        self.platformColor = colors.deep_purple
        self.scoreColor = colors.grey_overlay
        self.effectColor = colors.yellow
        self.platform = "square_yellow.png"
        self.bonus = "circle_yellow.png"
        self.id = 0
