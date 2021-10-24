from prison import Player


class NiceAgent(Player):
    """
    This is an nice player
    """
        
    def studentID(self):
        return "0"

    def agentName(self):
        return "Nice Player"

    def play(self, myHistory, oppHistory1, oppHistory2):
        return 0
