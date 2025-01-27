from Robot import *
class Cylindres:
    def __init__(self,Id,x,y,Type,Rayon=1):
        self.Id=Id
        self.Rayon=Rayon
        self.x=x
        self.y=y
        self.Type=Type

    def Distance(self,Robot):
        R=self.Rayon
        Xc=self.x
        Yc=self.y
        Xr=Robot.x
        Yr=Robot.y
        return ((Xc-Xr)**2+(Yc-Yr)**2)**0.5-R
    
    def __str__(self):
        return "id="+str(self.Id)+" x="+str(self.x)+" y="+str(self.y)+" Type="+str(self.Type)
        
        