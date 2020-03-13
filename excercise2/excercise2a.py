import gym
import numpy as np
import time
env = gym.make('CartPole-v0')
pvariance = 0.1 # variance of initial parameters
ppvariance = 0.02 # variance of perturbations
nhiddens = 5 # number of hidden neurons
population_size = 20
ninputs = env.observation_space.shape[0]
if (isinstance(env.action_space, gym.spaces.box.Box)):
    noutputs = env.action_space.shape[0]
else:
    noutputs = env.action_space.n


# initialize the training parameters randomly by using a gaussian distribution with average 0.0 and variance 0.1
# biases (thresholds) are initialized to 0.0
W1 = np.random.randn(nhiddens,ninputs) * pvariance
# first layer
W2 = np.random.randn(noutputs, nhiddens) * pvariance
# second layer
b1 = np.zeros(shape=(nhiddens, 1))
# bias first layer
b2 = np.zeros(shape=(noutputs, 1))
# bias second layer


for i_episode in range(population_size):
    observation = env.reset()
    for t in range(100):
        time.sleep(0.01)
        env.render()
        # print(observation)
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)
        # convert the observation array into a matrix with 1 column and ninputs rows
        observation.resize(ninputs,1)
        # compute the netinput of the first layer of neurons
        Z1 = np.dot(W1, observation) + b1
        # compute the activation of the first layer of neurons with the tanh function
        A1 = np.tanh(Z1)
        # compute the netinput of the second layer of neurons
        Z2 = np.dot(W2, A1) + b2
        # compute the activation of the second layer of neurons with the tanh function
        A2 = np.tanh(Z2)
        # if actions are discrete we select the action corresponding to the most activated unit
        if (isinstance(env.action_space, gym.spaces.box.Box)):
            action = A2
        else:
            action = np.argmax(A2)
env.close()

