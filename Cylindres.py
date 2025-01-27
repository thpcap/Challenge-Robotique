class Cylindres:
    def __init__(self,Id,x,y,Type,Rayon=1):
        self.Id=Id
        self.Rayon=Rayon
        self.x=x
        self.y=y
        self.Type=Type
    
    def __str__(self):
        return "id="+str(self.Id)+" x="+str(self.x)+" y="+str(self.y)+" Type="+str(self.Type)
        
        