# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------

from abc import ABC, abstractmethod

from components.value_manager import ValueManager

# Permet de gerer les langues du jeu


class Language(ABC):

    # name = ("en_text","fr_text")
    app_name = ("PyBall", "PyBall")
    high_score = ("Highscore score :", "Meilleur score :")
    tuto1 = ("Press space to start", "Espace pour commencer")
    tuto2 = ("P to pause", "P pour mettre en pause")
    tuto3 = ("R to restart", "R pour recommencer")

    @abstractmethod
    def getLang():  # Retourne l'id de la lanque du jeu
        return int(ValueManager.get("language", "0"))

    @abstractmethod
    def setLang(lang):  # Change l'id de la lanque du jeu
        ValueManager.save("language", str(lang))
