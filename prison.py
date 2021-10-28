"""
This Python module models the three-player Prisoner's Dilemma game.
We use the integer "0" to represent cooperation, and "1" to represent
defection.

Recall that in the 2-players dilemma, U(DC) > U(CC) > U(DD) > U(CD), where
we give the payoff for the first player in the list. We want the three-player game
to resemble the 2-player game whenever one player's response is fixed, and we
also want symmetry, so U(CCD) = U(CDC) etc. This gives the unique ordering

U(DCC) > U(CCC) > U(DDC) > U(CDC) > U(DDD) > U(CDD)

The payoffs for player 1 are given by the following matrix:

@author: akhtsang
Created on Feb 9, 2017
"""


from Agents.DittoAgent import DittoAgent
from Agents.MeanAgent import MeanAgent
from Agents.NiceAgent import NiceAgent
from Agents.RandomAgent import RandomPlayer

PAYOFF = [[[6, 3], [3, 0]], [[8, 5], [5, 2]]]

"""
So payoff[i][j][k] represents the payoff to player 1 when the first
player's action is i, the second player's action is j, and the
third player's action is k.

In this simulation, triples of players will play each other repeatedly in a
'match'. A match consists of about 100 rounds, and your score from that match
is the average of the payoffs from each round of that match. For each round, your
strategy is given a list of the previous plays (so you can remember what your 
opponent did) and must compute the next action.
 """


if __name__ == "__main__":
    """
    Replace one or two of these with your player!
    """
    from runTournament import scoreGame, runTournament, NPLAYERS

    NROUNDS = 200
    #
    # p1 = DittoAgent()
    # p2 = MeanAgent()
    # p3 = NiceAgent()
    #
    # s1, s2, s3 = scoreGame(p1, p2, p3, NROUNDS)
    # print("========== 3PD Results ==========")
    # print(p1.agentName(), " (", p1.studentID(), ") :", s1)
    # print(p2.agentName(), " (", p2.studentID(), ") :", s2)
    # print(p3.agentName(), " (", p3.studentID(), ") :", s3)
    # if p1.studentID() == "42" and p2.studentID() == "42" and p3.studentID() == "42":
    #     raise AssertionError("DANGER WILL ROBINSON: Make sure you replace one or two of the players with your agent!")

    # print the CSV for NRounds
    result_csv = ""
    for i in range(NROUNDS):
        result = runTournament(NPLAYERS)
        result_csv += ','.join(map(str, result)) + "\n"
    print(result_csv)
