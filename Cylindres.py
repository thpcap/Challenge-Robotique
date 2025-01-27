class Cylindres:
    def __init__(self,Id,x,y,Type,Rayon=1):
        self.Id=Id
        self.Rayon=Rayon
        self.x=x
        self.y=y
        self.Type=Type
        if(self.Type==1):
            self.Masse=1
            self.Valeur=1
        elif(self.Type==2):
            self.Masse=2
            self.Valeur=2
        elif(self.Type==3):
            self.Masse=2
            self.Valeur=3
        else:
            print("type de Cylindre non reconnu")
            self.Masse=-1
            self.Valeur=-1
    
    def __str__(self):
        return "id="+str(self.Id)+" x="+str(self.x)+" y="+str(self.y)+" Type="+str(self.Type)+" masse="+str(self.Masse)+" valeur="+str(self.Valeur)
        
        