from Agents.Player import Player


class DittoAgent(Player):
    """
    Agent Applies Tit-for-Tat Strategy
    """

    def studentID(self):
        return "2"

    def agentName(self):
        return "T4TAgent"

    def play(self, myHistory, oppHistory1, oppHistory2):

        round_number = len(myHistory)

        # cooperate initially
        if round_number == 0:
            return 0

        # defect if either defect player defects
        if (oppHistory1[round_number - 1] == 1) or (oppHistory2[round_number - 1] == 1):
            return 1

        # cooperate otherwise
        return 0
