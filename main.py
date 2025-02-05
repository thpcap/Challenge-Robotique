from Calcul import*
from GenerateMap import *
from Cylindres import *
from Robot import *

def main():
    generate(20)
    cylindres=Input_Map(input_link)
    cylindres2=[]
    cylindres3=[]
    for cylindre in cylindres:
        cylindres2.append(cylindre) 
        cylindres3.append(cylindre) 
    _,p = simulatePath((path(cylindres)), cylindres3)
    p=optimizePath(p)
    pathToFile(p)
    drawPath(p, cylindres2)
    print("finished")
    
main()