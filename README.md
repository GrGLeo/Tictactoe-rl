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
