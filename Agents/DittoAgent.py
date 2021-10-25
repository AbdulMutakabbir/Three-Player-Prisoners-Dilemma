from Agents.Player import Player
from random import random


class DittoAgent(Player):
    """
    Ditto applies Tit for Tat strategy as a player
    """

    def studentID(self):
        return "7"

    def agentName(self):
        return "DittoAgent"

    def play(self, myHistory, oppHistory1, oppHistory2):

        round_number = len(myHistory)

        # cooperate initially
        if round_number == 0:
            return 0

        # if either defect player defects till round 16
        if round_number <= 15:
            if (oppHistory1[round_number - 1] == 1) or (oppHistory2[round_number - 1] == 1):
                return 1
            else:
                return 0

        defect_rate_opponent_1 = sum(oppHistory1) / round_number
        defect_rate_opponent_2 = sum(oppHistory2) / round_number
        acceptable_defect_rate = 3 / round_number

        # defect based on player defect rate till round 50
        if round_number <= 50:
            if defect_rate_opponent_1 > acceptable_defect_rate or defect_rate_opponent_2 > acceptable_defect_rate:
                return 1
            else:
                return 0

        # cooperate mostly if the defect rate is less than 2%
        move = 1 if defect_rate_opponent_1 > 0.02 or defect_rate_opponent_2 > 0.02 else 0 if random() > 0.02 else 1
        return move
