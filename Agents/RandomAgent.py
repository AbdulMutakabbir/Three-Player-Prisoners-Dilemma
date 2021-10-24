from prison import Player
import random


class RandomPlayer(Player):
    """
    The randomPlayer chooses an action randomly.
    """

    def studentID(self):
        return "0.5"

    def agentName(self):
        return "Random Player"

    def play(self, myHistory, oppHistory0, oppHistory2):
        return random.randint(0, 1)
