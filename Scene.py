#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------
from abc import ABCMeta, abstractmethod
import Colors, Constants, math

#Cette classe abstraite permet de construire plus facilement les
#scenes. Le moteur GamePanel appel successivement Update() et Draw()
#de cette classe. Comme cette classe permet de construire les scenes
#alors les scenes seront affichÃ©es.

#OnCreate() est appelee un fois que les animations entrante est finie
#OnEnd() est appelee lorsque l'animation sortante est finie

#startscene() lance l'animation entrante
#stopscene() lance l'animation sortante

#update() met a jour la scene
#draw() dessine la mise a jour de la scene

#onEvent() redistribue les events du joueur

class Scene(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def onCreate(self):
        print("onCreate")

    @abstractmethod
    def startScene(self):
        print("startingScene")

    @abstractmethod
    def stopScene(self):
        print("stoppingScene")

    @abstractmethod
    def update(self):
        pass


    @abstractmethod
    def draw(self, fen):
        pass

    @abstractmethod
    def onEnd(self):
        pass

    @abstractmethod
    def onEvent(self, event):
        print("onEvent")


