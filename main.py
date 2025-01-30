from Calcul import*
from GenerateMap import *
from Cylindres import *
from Robot import *

generate(20)
cylindres=Input_Map(input_link)
cylindres2=[]
for cylindre in cylindres:
    cylindres2.append(cylindre)
robot=Robot()   
_,p = path(robot,cylindres)
pathToFile(p)
drawPath(p, cylindres2)
print("finished")