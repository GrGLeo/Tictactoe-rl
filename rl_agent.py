from game import Game
import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
from collections import deque

style.use("ggplot")

# Learning variable
EPISODE = 25_000
LEARNING_RATE = 0.5
DISCOUNT = 0.95
epsilon = 0.95
epsilon_decay = 0.999

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



win_loss = []
reward_saved = deque(maxlen=500)
rolling_avg = []

# Training loop
for ep in range(EPISODE):
    total_reward = 0
    env = Game()
    state = tuple(env.board.flatten())
    done = False
    while not done:
        # Exploitation
        if np.random.random() > epsilon:
            n = np.argmax(q_table[state])
            action = get_action(n)
        # Exploration
        else:
            n = np.random.randint(0,9)
            action = get_action(n)

        # Taking step
        illegal,new_state = env.move(*action)
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

        # Set up next step
        state=new_state
        total_reward += reward

    # Epsilon decay
    epsilon *= epsilon_decay
    # Keeping a 5% exploration while training
    epsilon = max(0.05,epsilon)

    if win:
        q_table[state][n] = 0
        print(f"We won at episode {ep}, total reward : {total_reward}")

    win_loss.append(1 if win else 0)
    reward_saved.append(total_reward)

    if len(reward_saved) == 500:
        rolling_avg.append(np.average(reward_saved))


fig,(ax1,ax2) = plt.subplots(1,2)
ax1.hist(win_loss)
ax1.set_title("Win/Loss ratio")
ax2.plot([i for i in range(EPISODE-499)],rolling_avg)
ax2.set_title("Rolling average reward")
plt.savefig("rewards.png")

with open('q_table.pkl','wb') as f:
    pickle.dump(q_table,f)
    print("Q_table saved successfully")
