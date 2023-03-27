from game import Game
import numpy as np


EPISODE = 40000
LEARNING_RATE = 0.1
DISCOUNT = 0.95
# Initializing the env
env = Game()

# Create q_table
q_table = {}
while len(q_table) != 3**9:
    q_table[tuple(np.random.randint(0,3,size=(9)))] = np.random.uniform(low=-1,high=1,size=9)

def get_action(n):
    if n == 0:
        return (0,0)
    if n == 1:
        return (0,1)
    if n == 2:
        return (0,2)
    if n == 3:
        return (1,0)
    if n == 4:
        return (1,1)
    if n == 5:
        return (1,2)
    if n == 6:
        return (2,0)
    if n == 7:
        return (2,1)
    if n == 8:
        return (2,2)


for ep in range(EPISODE):
    total_reward = 0
    env = Game()
    state = tuple(env.board.flatten())
    done = False
    while not done:
        n = np.argmax(q_table[state])
        action = get_action(n)
        illegal,new_state = env.move(*action)
        #print(env.board)
        done, reward, win = env.game_state()
        if illegal:
            reward -=5
            done=True

        # q_value update
        if not done:
            max_futur_q = np.max(q_table[new_state])
            current_q = q_table[state][n]
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE*(reward + DISCOUNT*max_futur_q)
            q_table[state][n] = new_q

        state=new_state
        total_reward += reward

        if win:
            print(f"We won at episode {ep}, total reward : {total_reward}")
