import math
from Cylindres import *

class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.mass = 0
        self.orientation = math.pi/2
        self.fuel = 10000
        self.b = 0.01
        self.b0 = 0.01
        self.alpha = 0.0698
        self.v0 = 1

    def vitesse(self):
        return self.v0 * math.exp(-self.alpha * self.mass)
    
    def consumption(self):
        return self.b * self.mass + self.b0

    def angle(self, cylindre):
        return math.atan((self.x-cylindre.x)/(self.y-cylindre.y)) - self.orientation
     
    def Distance(self, cylindre):
        return ((self.x-cylindre.x)**2+(self.y-cylindre.y)**2)**0.5-cylindre.Rayon