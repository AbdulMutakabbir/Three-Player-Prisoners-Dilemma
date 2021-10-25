# Three-Player-Prisoners-Dilemma

### Introduction 
In the game the Prisoners' Dilemma, the dominant strategy equilibrium is for agents to defect 
(i.e. confess) even though both agents would be better off cooperating with each other and 
keeping quiet. When we move to the repeated version of the game, however, the possibility of 
cooperation begins to appear.

A strategy in a repeated game specifies what action the agent should play in each state of the 
game, given all actions taken by all players in the previous rounds.

To add a minor complication to the game, the communication channel with the game is noisy. 

The objective of this Project is to develope an Agent/Player that will be able to perform best 
when competing with others in the Game.


### Literature Review
The below mention strategies were tested to find the best strategy:
 * [Nice Agent (Always Co-operates)](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/NiceAgent.py)
 * [Mean Agent (Always Defers)](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/MeanAgent.py)
 * [Random Agent (Co-operates and Defers Evenly)](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/RandomAgent.py)
 * Randomly Nicer Agent (Mostly Co-operates but also Defers)
 * Randomly Meaner Agent (Mostly Defers but also Co-operates)
 * Co-ordinated Agents (These agent only Co-operate when played against an agent of the Same type)
 
The Nice Agent will perform last when competing with agents of the other type since they will Defer
at some point in time and will cause the nice agent too loose. Although the Nice agent will 
outperform all the other when played agents of similar type.

The Mean agent is the clear winner in all matches it competes no matter what player it is against.
Although this strategy is good it will loose some points that can be gained through Co-operation.

All the Random Agents are similar with a variable degree of Co-operation and Defer. They will 
perform above or below average based on higher Defer rate of higher Co-operation rate respectively. 

Co-ordinated Agent have th e added advantage of the bonus Co-operation points that they will get when
performing with Agents of similar type. (Although similar to Nice agent but agent but a bit more 
thought out and strategic when competing with Mean players). They would also need to waist some rounds
trying to identifying each other when the communication channel is blind agents.


### Methodology
Considering the above general strategies an agent should be have its responses based on a tiered 
structure where in 
 * Tire 1: Copy other agents responses.
 * Tire 2: Co-operate based on a slightly larger Tolerance to Defer rate
 * Tire 3: Co-operate based on Defer rate
 * Tire 4: Co-operate less often based on Defer rate
 
> Defer Rate: The amount of times the opponent agent defers
 
Tire 1 is to copy the th e handshaking messages given by Co-ordinated agents and to become a part of 
them.

Tire 2 goes for a Tit-For-Tat strategy but with noise tolerance to ensure meaner agents don't get the 
best of you.

Tire 3 is similar to Tire 2 but will be less tolerant as it has a higher number of data points to 
determine the co-operation level of the competing agents.

Tire 4 the agents has less motivation to co-operate now since its the end of game any how.


### Agent Design
Based on the above mentioned methodology 
[Ditto Agent](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/blob/main/Agents/DittoAgent.py) 
was developed that has the following co-operation strategy.

![Agent Flowchart](https://raw.githubusercontent.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/main/assets/charts/Ditto_FlowChart.svg)

The round number are arbitrarily fixed but should be changes based on the number of rounds.


### Performance
Below you are given the "Scatter Plot" and the "Box Chart" of 200 times Ditto Agent competed with the 
above mentioned agents in 
[Literature Review](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma#literature-review).

![Scatter Plot](https://raw.githubusercontent.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/main/assets/charts/Tournment_ScatterPlot.png)
![Box Chart](https://raw.githubusercontent.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma/main/assets/charts/Tournment_BoxPlot.png)


### Results 
As seen in the [Performance Section](https://github.com/AbdulMutakabbir/Three-Player-Prisoners-Dilemma#performance) 
Ditto Agent perform as good as the best agent (Mean Agent).