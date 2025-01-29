import random
from Calcul import *
from GenerateMap import *
import datetime

def train(generations = 100, mutation = 1,  mutation_factor = 2, maps = 100):
    generate(20)
    cylindres=generateMap(20)
    robot=Robot()

    weights = list(getWeights().values())
    weights_list = []
    weights_list.append(weights)
    reward_list = []
    reward_list.append(path(robot, cylindres, True))
    ind_best = 0
    best_reward = reward_list[0]
    print(best_reward)
    for i in range(generations):
        weights = weights_list[ind_best]
        weights = generateRandomWeights(mutation, mutation_factor, weights)
        weights_list.append(weights)
        setWeights(weights)
        temp_rewards = []
        for j in range(maps):
            cylindres=generateMap(20)
            robot=Robot()
            temp_rewards.append(path(robot, cylindres, True))

        avg_reward = sum(temp_rewards)/len(temp_rewards)
        reward_list.append(avg_reward)
        if avg_reward > best_reward:
            best_reward = avg_reward
            ind_best = i+1
        if (i%100 == 0):
            print(str(avg_reward) + "  |   " + str(datetime.datetime.now()))
    print("\n")
    print(best_reward)
    print(reward_list[ind_best])
    print(weights_list[ind_best])


def generateRandomWeights(mutation, mutation_factor, weights):
    mutation_count = 0
    list_index = []
    for i in range(mutation):
        j = int(random.random()*len(weights))
        while j in list_index:
            j = int(random.randdom()*len(weights))
        weights[j] += random.random()*mutation_factor*2 - mutation_factor
    return weights

train(generations = 100000, mutation = 1, mutation_factor = 0.5)
