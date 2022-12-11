# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------
from abc import ABC, abstractmethod
import components.colors as colors, Constants, math

from components.object import Object

# Cette classe abstraite permet de construire plus facilement les
# scenes. Le moteur GamePanel appel successivement Update() et Draw()
# de cette classe. Comme cette classe permet de construire les scenes
# alors les scenes seront affichÃ©es.

# OnCreate() est appelee un fois que les animations entrante est finie
# OnEnd() est appelee lorsque l'animation sortante est finie

# startscene() lance l'animation entrante
# stopscene() lance l'animation sortante

# update() met a jour la scene
# draw() dessine la mise a jour de la scene

# onEvent() redistribue les events du joueur


class Scene(Object):
    def onCreate(self):
        pass

    def startScene(self):
        pass

    def stopScene(self):
        pass

    def update(self):
        super(Scene, self).update()

    def draw(self, fen):
        super(Scene, self).draw(fen)

    def onEnd(self):
        pass

    def onEvent(self, event):
        super(Scene, self).onEvent(event)
