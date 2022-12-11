# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------


import time, pygame
from objects.agent_player_controller import AgentPlayerController
from objects.keyboard_player_controller import KeyboardPlayerController
from objects.player import Player
from components.pyball import PyBall
from plugins.rays import RaysPlugin
import Constants
from plugins.stop import StopPlugin
from scenes.game_scene import GameScene


if __name__ == "__main__":

    #    player_pos = [50, Constants.screenHeight / 2 - 25]
    #    player_controller = AgentPlayerController(player_pos)
    #    player = Player(player_controller, player_pos[0], player_pos[1], 50, 50)
    #    waiting_for_stop = False
    #    pyball = PyBall(player=player)
    #
    #    def onStop(state, score):
    #        print("Score:", score, "End State:", state)
    #        waiting_for_stop = False
    #        pyball.restart(player)
    #        new_scene = GameScene(pyball.gamePanel)
    #        pyball.gamePanel.changeScene(new_scene)
    #
    #    raysPlugin = RaysPlugin()
    #    stopPlugin = StopPlugin(player_controller, onStop)
    #    pyball.registerPlugin(raysPlugin, "after")
    #    pyball.registerPlugin(stopPlugin, "after")

    pyball = PyBall()
    pyball.start()

    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            pyball.stop()
            break
