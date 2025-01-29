import random
import concurrent.futures
from Calcul import *
from GenerateMap import *
import datetime
from input import *
import numpy as np

def calculate_reward(mapid):
    # Generate new map and robot
    #cylindres = generateMap(20)
    input_link =int(mapid)
    cylindres=Input_Map('test_Maps\donnees-map-'+str(input_link)+'.txt')
    robot = Robot()

    # Calculate reward
    reward = path(robot, cylindres, True)
    return reward

def train(generations=100, mutation=1, mutation_factor=1, maps=100):
    # Generate initial map and robot
    #generate(20)
    #cylindres = generateMap(20)
    cylindres= Input_Map('map.csv')
    robot = Robot()

    # Initialize weights and rewards
    weights = list(getWeights().values())
    weights_list = [weights]
    first_reward = path(robot, cylindres, True)
    print(first_reward)
    reward_list = [first_reward]

    for generation in range(generations):
        weights=weights_list[reward_list.index(max(reward_list))]
        new_reward_list = []
        weights = [w + random.uniform(-mutation, mutation) * mutation_factor for w in weights]
        setWeights(weights)
        with concurrent.futures.ThreadPoolExecutor(10) as executor:
            futures = [executor.submit(calculate_reward,i+1) for i in range(maps)]
            for future in concurrent.futures.as_completed(futures):
                reward = future.result()
                new_reward_list.append(reward)

        # Select the average weights
        avg_reward=np.mean(new_reward_list)
        weights_list.append(weights)
        reward_list.append(avg_reward)

        # Reduce mutation factor over time
        mutation_factor *= (generations-1)/generations

        # Print progress
        print(f"Generation {generation + 1}/{generations}, Avg Reward: {avg_reward}, Mutation Factor {mutation_factor}, {generation/generations}%")

    # Save the best weights
    setWeights(weights)
    print("Best generation:", reward_list.index(max(reward_list)) )
    print("Best weights:")
    for w in weights:
        keys_w=getWeightsKeys()
        print("\""+keys_w[weights.index(w)]+"\":"+str(w),end=",")
    print("Best reward:", max(reward_list))

    return weights_list, reward_list

if __name__ == "__main__":
    train(100000,mutation=20,maps=10)
