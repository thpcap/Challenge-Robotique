from Cylindres import *
from input import *
from Robot import *
from links import *
from Colision import *
from GenerateMap import *
import math
import matplotlib.pyplot as plt
import matplotlib.patches as pat


weights={
    "distance":-31.73641784169041,"reward":14.7179371699533,"mass":30.331067567610134,"collision":-2.3138877444930697,"variation":6.159866326376777
}

def getWeights():
    return weights

def getWeightsKeys():
    return list(weights.keys())

def setWeights(_weights):
    ind = 0
    for name in weights.keys():
        weights[name] = _weights[ind]
        ind += 1

def h(robot, cylindre):
    if robot.consumption()*robot.Distance(cylindre)>robot.fuel:
        return -float("inf")

    return robot.Distance(cylindre)*weights["distance"]+weights["variation"]*robot.fuel + cylindre.Valeur * weights["reward"] + cylindre.Masse*weights["mass"]

def path(robot, cylindres):
    path = []
    time = 0
    while (len(cylindres)):
        #calcule le meilleur cylindre à  atteindre
        best = cylindres[0]
        best_value = 0
        for cylindre in cylindres:
            value = h(robot, cylindre)
            for cyl in cylindres:
                if cyl.Id!=cylindre.Id:
                    if intersectSegmentCircle(robot,cylindre,cyl):
                        value+=cyl.Valeur*weights["reward"]+cyl.Masse*weights["mass"]+weights["collision"]
            if best_value < value:
                best_value = value
                best = cylindre
        cylindres.remove(best)
        #calcule la nouvelle position du robot et le deplassement
        dist = robot.Distance(best)
        angl = robot.angle(best)
        
        for cyl in cylindres:
            if intersectSegmentCircle(robot,best,cyl):
                cylindres.remove(cyl)         
                        
        robot.orientation += angl
        robot.x += (math.cos(math.pi/2 - robot.orientation) * dist)
        robot.y += (math.sin(math.pi/2 - robot.orientation) * dist)

        path.append(best)       
    return path

def simulatePath(path):
    path = []
    time = 0
    for point in path:
        #calcule la nouvelle position du robot et le deplassement
        dist = robot.Distance(point)
        angl = robot.angle(point)
        
        for cyl in cylindres:
            if cyl.Id!=point.Id:
                if intersectSegmentCircle(robot,point,cyl):
                    robot.reward += cyl.Valeur
                    robot.mass += cyl.Masse
                    cylindres.remove(cyl)         
                        
        robot.orientation += angl
        robot.fuel -= robot.consumption() * dist
        time += dist/robot.vitesse()
        if (robot.fuel < 0 and time>=600):
            break

        robot.mass += point.Masse
        robot.reward+=point.Valeur
        robot.x += (math.cos(math.pi/2 - robot.orientation) * dist)
        robot.y += (math.sin(math.pi/2 - robot.orientation) * dist)

        path.append(point)    
    return (robot.reward, path)

def drawPath(path, cylindres):
    robot = Robot()
    # Initialize variables for graph
    reward_list = [0]
    mass_list = [0]
    time = 0
    times = [0]
    fuel_list=[robot.fuel]
    # Initialize variables for plot
    _, ax = plt.subplots()
    plt.xlim(-5,30)
    plt.ylim(-5,25)
    plt.grid(linestyle='--')
    ax.set_aspect(1)
    nbCyl=len(cylindres)
    for Cyl in cylindres:
        circle = plt.Circle((Cyl.x,Cyl.y ), Cyl.Rayon+0.05, color='orange')
        circle2 = plt.Circle((Cyl.x,Cyl.y ), 1, color=Cyl.color)
        ax.add_artist(circle)
        ax.add_artist(circle2)
    ax.add_artist(pat.Rectangle((-0.5, -0.5), 1, 1, color = 'black'))
    ax.add_artist(pat.Rectangle((-0.4, -0.4), 0.8, 0.8, color = 'magenta'))
    ax.plot((1,0),(0,0),color='magenta')

    for point in path:
        total_value = 0
        total_mass = 0
        for cyl in cylindres:
            if cyl.Id!=point.Id:
                if intersectSegmentCircle(robot,point,cyl):
                    total_value += cyl.Valeur
                    total_mass += cyl.Masse
                    cylindres.remove(cyl)
                    circle = plt.Circle((cyl.x,cyl.y ), cyl.Rayon/3, color='white')
                    ax.add_artist(circle)
        
        x=robot.x
        y=robot.y
        dist = robot.Distance(point)
        angl = robot.angle(point)
        robot.orientation += angl
        robot.fuel -= robot.consumption() * dist
        
        circle = plt.Circle((point.x,point.y ), point.Rayon/3, color='white')
        ax.add_artist(circle)

        robot.reward+=point.Valeur + total_value
        robot.mass += point.Masse + total_mass
        robot.x += (math.cos(math.pi/2 - robot.orientation) * dist)
        robot.y += (math.sin(math.pi/2 - robot.orientation) * dist)
        cylindres.remove(point)
        time += dist/robot.vitesse()
        fuel_list.append(robot.fuel)
        times.append(time)
        reward_list.append(robot.reward)
        mass_list.append(robot.mass)

        ax.plot((robot.x,x),(robot.y,y),color='black')
        circle = plt.Circle((robot.x,robot.y ), 0.1, color='black')
        ax.add_artist(circle)

    # Display graphs and plots
    plt.title('path reward='+str(robot.reward)+" nbCyl="+str(nbCyl) + " fuel="+str(robot.fuel), fontsize=8)
    _, axs = plt.subplots(2)
    ax2=axs[0]
    ax3=axs[1]
    plt.title('reward/mass'+str(time), fontsize=8)
    ax2.plot(times, reward_list, color="blue")
    ax3.plot(times, fuel_list, 0, color="black")
    plt.show()

def pathToFile(path):
    robot = Robot()
    Output_File = open(output_link,mode="w")
    Output_Str=""

    for cyl in path:
        dist = robot.Distance(cyl)
        angl = robot.angle(cyl)
        robot.orientation += angl
        robot.fuel -= robot.consumption() * dist
        robot.reward+=cyl.Valeur
        robot.mass += cyl.Masse
        robot.x += (math.cos(math.pi/2 - robot.orientation) * dist)
        robot.y += (math.sin(math.pi/2 - robot.orientation) * dist)

        #add Commands for the Robot
        Output_Str+="TURN "+str(-angl*(180/math.pi))+"\n"
        Output_Str+="GO "+str(dist)+"\n"

    Output_Str+="FINISH"
    Output_File.write(Output_Str)
    Output_File.close()