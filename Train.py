import random
from Calcul import *

def train(generations = 100, mutation = 1,  mutation_factor = 2, maps = 10):
    #generate(20)
    cylindres=Input_Map(input_link)
    robot=Robot()

    weights = getWeights().value()
    weights_list.append(weights)
    reward_list = []
    reward_list.append(path(robot, cylindres, True))
    ind_best = 0
    best_reward = reward_list[0]
    for i in range(generations):
        robot=Robot()
        weights = generateRandomWeights(mutation, mutation_factor, weights)
        weights_list.append(weights)
        setWeights(weights)
        temp_reward = path(robot, cylindres, True)
        reward_list.append(temp_reward)
        if temp_reward > best_reward:
            best_reward = temp_reward
            ind_best = i
    
    print(reward_list[ind_best])
    print(weights_list[ind_best])


def generateRandomWeights(mutation, mutation_factor, weights):
    mutation_count = 0
    list_index = []
    for i in range(mutation):
        j = int(random.randdom()*len(weights))
        while j in list_index:
            j = int(random.randdom()*len(weights))
        weights[j] += random.random()*mutation_factor*2 - mutation_factor
    return weights

train()