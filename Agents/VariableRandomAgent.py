from Agents.Player import Player
from random import random


class NiceRandomPlayer(Player):
    """
    The randomPlayer chooses co-operation more often .
    """

    def studentID(self):
        return "0.3"

    def agentName(self):
        return "Random Player"

    def play(self, myHistory, oppHistory0, oppHistory2):
        move = 1 if random() <= 0.3 else 0
        return move


class MeanRandomPlayer(Player):
    """
    The randomPlayer chooses defect more often .
    """

    def studentID(self):
        return "0.3"

    def agentName(self):
        return "Random Player"

    def play(self, myHistory, oppHistory0, oppHistory2):
        move = 0 if random() <= 0.3 else 1
        return move