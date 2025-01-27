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
        return self.v0 * math.exp(-alpha * self.mass)
    
    def consumption(self):
        return sefl.b * self.mass + self.b0

    def angle(self, cylindre):
        dot = self.x*cylindre.x + self.y*cylindre.y
        norm_product = (self.x**2 + self.y**2)**0.5 + (cylindre.x**2 + cylindre.y**2)*0.5
        return math.acos(dot/norm_product)
     
    def Distance(self, cylindre):
        return ((self.x-cylindre.x)**2+(self.y-cylindre.y)**2)**0.5-cylindre.Rayon