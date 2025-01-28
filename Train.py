import random
from Calcul import *

def train(generations = 100, mutation = 1,  mutation_factor = 2, maps = 10):
    generate(20)
    cylindres=Input_Map(input_link)
    robot=Robot() 

    weights = getWeights().value()
    weights_list.append(weights)
    for i in range(generations):
        reward = path(robot, cylindres, True)
        generateRandomWeights(mutation, mutation_factor, weights)


def generateRandomWeights(mutation, mutation_factor, weights):
    result = weights
    for i in range(mutation):
        pass

def test(a):
    a+1

test1 = 0
test(test1)
print(test1)