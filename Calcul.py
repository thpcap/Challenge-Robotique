from Cylindres import *
from input import *
from Robot import *
from links import *
from Colision import *
from GenerateMap import generate
import math
import matplotlib.pyplot as plt
import matplotlib.patches as pat


weights={
    "distance": -2,
    "reward": 8,
    "mass": -2
}

def h(robot, cylindre):
    return robot.Distance(cylindre)*weights["distance"] + cylindre.Valeur * weights["reward"] + cylindre.Masse*weights["mass"]

def path(robot, cylindres, train=False):
    #ouvre le fichier d'output
    with open(output_link,mode="w")as Output_File:
        Output_Str=""
        robot = Robot()
        reward_list = [0]
        mass_list = [0]
        if(not train) : 
            _, ax = plt.subplots()
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

        time = 0
        times = [0]
        while (robot.fuel > 0 and len(cylindres) and time<=600):
            #calcule le meilleur cylindre à  atteindre
            best = cylindres[0]
            best_value = 0
            for cylindre in cylindres:
                value = h(robot, cylindre)
                for cyl in cylindres:
                    if cyl.Id!=cylindre.Id:
                        if intersectSegmentCircle(robot,cylindre,cyl):
                            value+=cyl.Valeur*weights["reward"]+cyl.Masse*weights["mass"]
                if best_value < value:
                    best_value = value
                    best = cylindre
            cylindres.remove(best)
            x=robot.x
            y=robot.y
            #calcule la nouvelle position du robot et le deplassement
            dist = robot.Distance(best)
            angl = robot.angle(best)
            
            for cyl in cylindres:
                    if cyl.Id!=best.Id:
                        if intersectSegmentCircle(robot,best,cyl):
                            robot.reward += cyl.Valeur
                            robot.mass += cyl.Masse
                            cylindres.remove(cyl)                            
                            
            robot.reward+=best.Valeur
            robot.orientation += angl
            robot.fuel -= robot.consumption() * dist
            robot.mass += best.Masse
            robot.x += (math.cos(math.pi/2 - robot.orientation) * dist)
            robot.y += (math.sin(math.pi/2 - robot.orientation) * dist)
            time += dist/robot.vitesse()

            times.append(time)
            reward_list.append(robot.reward)
            mass_list.append(robot.mass)
            if(not train) : 
                ax.plot((robot.x,x),(robot.y,y),color='black')
                circle = plt.Circle((robot.x,robot.y ), 0.1, color='black')
                ax.add_artist(circle)

            #add Commands for the Robot
            Output_Str+="TURN "+str(-angl*(180/math.pi))+"\n"
            Output_Str+="GO "+str(dist)+"\n"

        plt.title('path '+str(robot.reward), fontsize=8)
        if(not train) : 
            _, axs = plt.subplots(2)
            ax2=axs[0]
            ax3=axs[1]
            plt.title('reward/mass', fontsize=8)
            ax2.plot(times, reward_list, color="blue")
            ax3.plot(times, mass_list, 0, color="black")            
        
        Output_Str+="FINISH"
        Output_File.write(Output_Str)
        Output_File.close()
        if(not train) : plt.show()
        return robot.reward
        

generate(30)
cylindres=Input_Map(input_link)
robot=Robot()   
path(robot,cylindres)