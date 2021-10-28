# Three-Player-Prisoners-Dilemma

### Introduction 
In the game the Prisoners' Dilemma, the dominant strategy equilibrium is for agents to defect 
(i.e. confess) even though both agents would be better off cooperating with each other and 
keeping quiet. When we move to the repeated version of the game, however, the possibility of 
cooperation begins to appear.

A strategy in a repeated game specifies what action the agent should play in each state of the 
game, given all actions taken by all players in the previous rounds.

To add a minor complication to the game, the communication channel with the game is noisy. 

The objective of this project is to develop an Agent/Player that will be able to perform best 
when competing with others in the game.


### Literature Review
The following strategies were tested to arrive at the best strategy:
 * [Nice Agent (Always Co-operates)](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/NiceAgent.py)
 * [Mean Agent (Always Defers)](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/MeanAgent.py)
 * [Random Agent (Co-operates and Defers Evenly)](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/RandomAgent.py)
 * [Randomly Nicer Agent (Mostly Co-operates but also Defers)](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/VariableRandomAgent.py)
 * [Randomly Meaner Agent (Mostly Defers but also Co-operates)](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/VariableRandomAgent.py)
 * Co-ordinated Agents (These agents only Co-operate when played against an agent of the same type)
 
The Nice Agent will perform last when competing with agents of the other type since they will Defer
at some point in time and will cause the Nice Agent to lose. Although the Nice Agent will 
outperform all the others when played against agents of similar type.

The Mean Agent is the clear winner in all matches it competes in, no matter what player it is against.
Although this strategy is good, it will lead to losing some points that can be gained through Co-operation.

All the Random Agents are similar with a variable degree of Co-operation and Defer. They will 
perform above or below average based on higher Defer rate or higher Co-operation rate respectively. 

Co-ordinated Agents have the added advantage of bonus Co-operation points that they will get when
performing with agents of similar type. (Although similar to Nice Agent but a bit more 
thought-out and strategic when competing with Mean players). They would also need to waste some rounds
trying to identifying each other when the communication channel is blind toward agents.


### Methodology
Considering the above general strategies, an agent should have its responses based on a tiered 
structure wherein 
 * Tier 1: Copy other agents responses.
 * Tier 2: Co-operate based on a slightly larger Tolerance to Defer rate
 * Tier 3: Co-operate based on Defer rate
 * Tier 4: Co-operate less often based on Defer rate
 
> Defer Rate: The amount of times the opponent agent defers
 
![Agent Tiers](https://raw.githubusercontent.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/main/assets/charts/Agent%20Tiers.png)
Tier 1 is to copy the handshaking messages given by Co-ordinated Agents and to become a part of 
them.

Tier 2 goes for a Tit-For-Tat strategy but with noise tolerance to ensure Meaner Agents do not get the 
best of the agent.

Tier 3 is similar to Tier 2 but will be less tolerant as it has a higher number of data points to 
determine the co-operation level of the competing agents.

Tier 4 is when the agent has less motivation to co-operate now since it's the end of game anyhow.


### Agent Design
Based on the above mentioned methodology 
[Ditto Agent](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/DittoAgent.py) 
was developed and it has the following Co-operation strategy.

![Agent Flowchart](https://raw.githubusercontent.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/main/assets/charts/Ditto_FlowChart.png)

The round numbers are arbitrarily fixed and should be changed based on the number of rounds.


### Performance
The "Scatter Plot" and the "Box Chart" of 200 times Ditto Agent competed with the 
above mentioned agents is given in the following:
[Literature Review](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma#literature-review).

![Scatter Plot](https://raw.githubusercontent.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/main/assets/charts/Tournment_ScatterPlot.png)
![Box Chart](https://raw.githubusercontent.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/main/assets/charts/Tournment_BoxPlot.png)


### Results 
As seen in the [Performance Section](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma#performance) 
Ditto Agent performs as good as the best agent (Mean Agent).
