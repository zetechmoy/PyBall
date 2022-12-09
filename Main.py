#-------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
#-------------------------------------------------------------------------------


import time
from PyBall import PyBall
from RaysPlugin import RaysPlugin
import Constants



if __name__ == '__main__':

    raysPlugin = RaysPlugin()
    
    pyball = PyBall()
    pyball.addPlugin(raysPlugin)
    pyball.start()

    # Handle signals
    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            pyball.stop()
            break