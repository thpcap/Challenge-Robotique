import random
import concurrent.futures
from Calcul import *
from GenerateMap import *
import datetime
from input import *
import numpy as np
import time


def calculate_reward(mapid):
    # Generate new map and robot
    #cylindres = generateMap(20)
    input_link = int(mapid)
    cylindres=Input_Map('test_Maps\donnees-map-'+str(input_link)+'.txt')

    # Calculate reward
    cylindres2=[]
    cylindres3=[]
    for cylindre in cylindres:
        cylindres2.append(cylindre)
        cylindres3.append(cylindre) 

    reward, p = simulatePath((path(cylindres)), cylindres2)
    reward,_ = simulatePath(optimizePath(p), cylindres3)
    return reward

def train(generations=100, mutation=1, mutation_factor=1, maps=10):
    # Generate initial map and robot
    #generate(20)
    #cylindres = generateMap(20)
    # Initialize weights and rewards
    weights = list(getWeights().values())
    weights_list = [weights]
    new_reward_list = []
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(10) as executor:
            futures = [executor.submit(calculate_reward,i+1) for i in range(maps)]
            for future in concurrent.futures.as_completed(futures):
                reward = future.result()
                new_reward_list.append(reward)

    # Select the average weights
    first_reward=np.mean(new_reward_list)
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

        # Calculate elapsed time and estimated remaining time
        elapsed_time = time.time() - start_time
        remaining_time = (elapsed_time / (generation + 1)) * (generations - (generation + 1))


        # Print progress
        print(f"Generation {generation + 1}/{generations}, Avg Reward: {round(avg_reward, 3)}, Mutation Factor {round(mutation_factor, 5)}, best reward: {max(reward_list)}, Estimated time remaining: {int(remaining_time / 60)} minutes, {round(generation / generations * 100, 4)}%,")

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
    train(100_000,mutation=50)

