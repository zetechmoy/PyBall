# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	09/12/2022
# -------------------------------------------------------------------------------

from components.object import Object


class Plugin(Object):
    def update(self):
        super(Plugin, self).update()

    def draw(self, fen):
        super(Plugin, self).draw(fen)

    def onEvent(self, event):
        super(Plugin, self).onEvent(event)
