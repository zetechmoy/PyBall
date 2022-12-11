# -------------------------------------------------------------------------------
# Author:      	Théo Guidoux
# Mail : 		theoguidoux@gmail.com
# Created:     	04/10/2015
# -------------------------------------------------------------------------------
from abc import abstractmethod

from components.value_manager import ValueManager


class ScoreManager(object):
    @abstractmethod
    def save(score):
        ValueManager.save("hscore", score)

    @abstractmethod
    def get():
        return int(ValueManager.get("hscore", "0"))
