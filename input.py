import csv
from Cylindres import *
def Input_Map(Map_CSV_Path):
    with open(Map_CSV_Path) as csv_file:        
        Cylindres_dic= csv.reader(csv_file, delimiter=" ")
        Cylindres_dic2=[]
        for row in Cylindres_dic:
            row2=[]
            for val in row:
                if(val!=""):
                    row2.append(val)
            Cylindres_dic2.append(row2)
        map=[]
        i=0
        for row in Cylindres_dic2:
            i+=1
            map.append(Cylindres(x=float(row[0]),y=float(row[1]),Type=int(float(row[2])),Id=i))           
        csv_file.close()
        return map