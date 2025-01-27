from Cylindres import *
from input import *
from Robot import *
import math
import matplotlib as plt
from matplotlib.patches import Circle

weights={
    "distance": 1,
    "reward": 1,
    "mass": 1
}

def h(robot, cylindre):
    return robot.distance(cylindre)*weights["distance"] + cylindre.Recompense * weights["reward"] + cylindre.Masse*weights["mass"]

def path(robot, cylindres):
    #ouvre le fichier d'output
    with open("output.txt",mode="w")as Output_File:
        Output_Str=""
        robot = Robot()
        for Cyl in cylindres:
            print(Cyl)
        path = []

        while robot.fuel > 0:
            #calcule le meilleur cylindre à  atteindre
            best = Cylindres()
            best_value = 0
            for cylindre in cylindres:
                value = h(robot, cylindre)
                if best_value < value:
                    best_value = value
                    best = cylindre
            path.append(best)
            cylindres.remove(best)

            #calcule la nouvelle position du robot et le deplassement
            dist = robot.distance(best)
            robot.orientation += robot.angle(cylindre)
            robot.fuel = robot.consumption * dist
            robot.mass += best.Masse
            robot.x = math.cos(math.pi/2 - angle) * dist
            robot.y = math.sin(math.pi/2 - angle) * dist
            
            #add Commands for the Robot
            Output_Str+="TURN "+str(robot.angle(cylindre))+"\n"
            Output_Str+="GO "+str(dist)+"\n"
            
        Output_Str+="FINISH"
        Output_File.write(Output_Str)
        Output_File.close()