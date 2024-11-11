import gridworlds           # import to trigger registration of the environment
import gymnasium as gym

# create instance
env = gym.make("gridworld-v0")
env.reset()

# test example
sum_rewards = 0
for i in range(10000):
    _, rew, _, _, _ = env.step(env.action_space.sample())
    sum_rewards += rew

print("Summed rewards over 10.000 episodes: ", sum_rewards)
