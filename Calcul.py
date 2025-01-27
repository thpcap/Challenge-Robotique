from Cylindres import *
from input import *
from Robot import *

weights={
    "distance": 1,
    "reward": 1,
    "mass": 1
}

def h(cylindre):
    return robot.distance(cylindre)*weights["distance"] + cylindre.Recompense * weights["reward"] + cylindre.Masse*weights[mass]

def path(robot, cylindres):
    cylindres = input.Input_Map("map.csv")
    robot = input.Input_Robot("") #TODO
    path = []

    while robot.consumption() > 0:
        best = Cylindres()
        best_value = 0
        for cylindre in cylindres:
            value = h(cylindre)
            if best_value < value:
                best_value = value
                best = cylindre
        path.append(best)

        robot.fuel = robot.consumption * robot.distance(best)
        robot.mass += best.Masse
        