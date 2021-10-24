from prison import Player


class MeanAgent(Player):
    """
    This is an mean player
    """
        
    def studentID(self):
        return "1"

    def agentName(self):
        return "Mean Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        return 1
