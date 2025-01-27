class Cylindres:
    def __init__(self,Id,x,y,Type,Rayon=1):
        self.Id=Id
        self.Rayon=Rayon
        self.x=x
        self.y=y
        self.Type=Type
    
    def __str__(self):
        return "x="+self.x+" y="+self.y+" Type="+self.Type
        
        