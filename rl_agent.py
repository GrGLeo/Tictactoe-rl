from game import Game
import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style

style.use("ggplot")

# Learning variable
EPISODE = 10_000
LEARNING_RATE = 0.5
DISCOUNT = 0.95

# Initializing the env
env = Game()

# Create q_table
q_table = {}
while len(q_table) != 3**9:
    q_table[tuple(np.random.randint(0,3,size=(9)))] = np.random.uniform(low=-1,high=0,size=9)


# 9 action possible, one for every position on the board
def get_action(n):
    actions = {0:(0,0), 1:(0,1), 2:(0,2),
               3:(1,0), 4:(1,1), 5:(1,2),
               6:(2,0), 7:(2,1), 8:(2,2)}
    return actions[n]



reward_saved = []

# Training loop
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

        # Penalty for making an illegal move
        if illegal:
            reward -=5
            done=True

        # Update q_value with bellman equation
        if not win:
            max_futur_q = np.max(q_table[new_state])
            current_q = q_table[state][n]
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE*(reward + DISCOUNT*max_futur_q)
            q_table[state][n] = new_q

        state=new_state
        total_reward += reward
    if win:
        q_table[state][n] = 0
        print(f"We won at episode {ep}, total reward : {total_reward}")

    reward_saved.append(total_reward)

fig,axes = plt.subplots(1,2)
axes[0].hist(reward_saved)
axes[1].plot([i for i in range(EPISODE)],reward_saved)
plt.savefig("rewards.png")
with open('q_table.pkl','wb') as f:
    pickle.dump(q_table,f)
    print("Q_table saved successfully")
