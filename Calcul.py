from Cylindres import *
from input import *
from Robot import *
import math
import matplotlib.pyplot as plt
import matplotlib.patches as pat

weights={
    "distance": -0.5,
    "reward": 1,
    "mass": -1
}

def h(robot, cylindre):
    return robot.Distance(cylindre)*weights["distance"] + cylindre.Valeur * weights["reward"] + cylindre.Masse*weights["mass"]

def path(robot, cylindres):
    #ouvre le fichier d'output
    with open("output.txt",mode="w")as Output_File:
        Output_Str=""
        robot = Robot()
        fig, ax = plt.subplots()
        plt.xlim(-5,30)
        plt.ylim(-5,25)
        plt.grid(linestyle='--')
        ax.set_aspect(1)
        for Cyl in cylindres:
            circle = plt.Circle((Cyl.x,Cyl.y ), Cyl.Rayon, color='black')
            circle2 = plt.Circle((Cyl.x,Cyl.y ), Cyl.Rayon-0.1, color=Cyl.color)
            ax.add_artist(circle)
            ax.add_artist(circle2)
        ax.add_artist(pat.Rectangle((-0.5, -0.5), 1, 1, color = 'black'))
        ax.add_artist(pat.Rectangle((-0.4, -0.4), 0.8, 0.8, color = 'magenta'))
        ax.plot((1,0),(0,0),color='magenta')
        path = []

        while (robot.fuel > 0 and len(cylindres)):
            #calcule le meilleur cylindre à  atteindre
            best = cylindres[0]
            best_value = 0
            for cylindre in cylindres:
                value = h(robot, cylindre)
                if best_value < value:
                    best_value = value
                    best = cylindre
            path.append(best)
            cylindres.remove(best)
            x=robot.x
            y=robot.y
            #calcule la nouvelle position du robot et le deplassement
            dist = robot.Distance(best)
            angl=robot.angle(best)

            robot.orientation += angl
            robot.fuel = robot.consumption() * dist
            robot.mass += best.Masse
            robot.x += (math.cos(math.pi/2 - robot.orientation) * dist)
            robot.y += (math.sin(math.pi/2 - robot.orientation) * dist)
            ax.plot((robot.x,x),(robot.y,y),color='black')

            #add Commands for the Robot
            Output_Str+="TURN "+str(-angl*(180/math.pi))+"\n"
            Output_Str+="GO "+str(dist)+"\n"            
        Output_Str+="FINISH"
        Output_File.write(Output_Str)
        Output_File.close()
        plt.title('path', fontsize=8)
        plt.show()
     
cylindres=Input_Map("C:\CHALLENGE\donnees-map.txt")

robot=Robot()   
path(robot,cylindres)