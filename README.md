# Simple implementation of reinforcement Learning

## TicTacToe Game

I first build a simple tictactoe game, on a 3x3 board, where a player input an x and y to marks a place. Then a bot will place a marks randomly
on an empty space. </br>
The marks are noted as 1 for the player, 2 for the bot, and 0s are empty space.</br>
If the player put a mark on an already marked spot, it will results in an illegal move and the game will be lost.

## Reinforcement learning

### Q table

The q table is a dictionnary with 19,683 keys, one for every state possible of the game.</br>
The values for each key is a vector of dimesnion 9, one for every action possible. The q value are initialized randomly.

### Rewards

The reward are shaped as follow:
- +10 for winning
- -10 for lossing
- -1 for taking an action
- -5 for an illegal move

### Bellman equation

To solve this environment we will use the bellman equation to udpate the Q value for a given state </br>
At each step, we will update the Q value, based on the new state of the game, the reward given by the step </br>
and the Q value of the previous step. </br>

<pre><code>new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE*(reward + DISCOUNT*max_futur_q)
</code></pre>

### Training the agent

As the q table is rather large, we will need a high number of episode, number of time the game will be play
and using both exploration and exploitation to find an optimal way of winning the game.</br>
We will use a exploration value : γ = 0.95 and a decay of 0.999. While maintaining a minimun γ = 0.05
to still have a minimun 5% chance of testing new move for each step.

With hundred thousand of episode to train, our agent start to have good results.
![alt text ](rewards.png)

## Results

After training for hundred thousand of episode the agent is able to win 96% of the time.</br>
The agent, q_table is saved in a pickle file</br>
To load the agent :
<pre><code>with open("q_table.pkl", "rb") as f:
    q_table = pickle.load(f)
</code></pre>
