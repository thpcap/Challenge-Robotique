import random
import concurrent.futures
from Calcul import *
from GenerateMap import *
import datetime
from input import *

def calculate_reward(weights, mutation, mutation_factor):
    # Mutate weights
    new_weights = [w + random.uniform(-mutation, mutation) * mutation_factor for w in weights]
    setWeights(new_weights)

    # Generate new map and robot
    #cylindres = generateMap(20)
    input_link =int(random.choice(range(1,10)))
    cylindres=Input_Map('test_Maps\donnees-map-'+str(input_link)+'.txt')
    robot = Robot()

    # Calculate reward
    reward = path(robot, cylindres, True)
    return new_weights, reward

def train(generations=100, mutation=1, mutation_factor=2, maps=100):
    # Generate initial map and robot
    generate(20)
    cylindres = generateMap(20)
    robot = Robot()

    # Initialize weights and rewards
    weights = list(getWeights().values())
    weights_list = [weights]
    reward_list = [path(robot, cylindres, True)]

    for generation in range(generations):
        new_weights_list = []
        new_reward_list = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(calculate_reward, weights, mutation, mutation_factor) for _ in range(maps)]
            for future in concurrent.futures.as_completed(futures):
                new_weights, reward = future.result()
                new_weights_list.append(new_weights)
                new_reward_list.append(reward)

        # Select the best weights
        best_index = new_reward_list.index(max(new_reward_list))
        weights = new_weights_list[best_index]
        weights_list.append(weights)
        reward_list.append(new_reward_list[best_index])

        # Reduce mutation factor over time
        mutation_factor *= 0.99

        # Print progress
        print(f"Generation {generation + 1}/{generations}, Best Reward: {new_reward_list[best_index]},mutation factor {mutation_factor}")

    # Save the best weights
    setWeights(weights)
    print("Best weights:", weights)
    print("Best reward:", max(reward_list))

    return weights_list, reward_list

if __name__ == "__main__":
    train(100,maps=100)