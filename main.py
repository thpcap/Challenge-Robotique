from Calcul import*
from GenerateMap import *
from Cylindres import *
from Robot import *

generate(20)
cylindres=Input_Map(input_link)
robot=Robot()   
_,p = path(robot,cylindres)
pathToFile(p)
cylindres=Input_Map(input_link)
drawPath(p, cylindres)
print("finished")