from Calcul import*
from GenerateMap import *
from Cylindres import *
from Robot import *

generate(20)
cylindres=Input_Map(input_link)
robot=Robot()   
path(robot,cylindres)
print("finished")