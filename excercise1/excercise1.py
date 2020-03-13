import gym
import time

gym.logger.set_level(40)

env = gym.make('CartPole-v0')

print(env.action_space)

print(env.observation_space)
print(env.observation_space.low)
print(env.observation_space.high)

env.reset()

steps = 200
for _ in range(steps):
    time.sleep(0.01)
    
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)

env.close()
