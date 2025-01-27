import csv
from Cylindres import *
def Input_Map(Map_CSV_Path):
    with open(Map_CSV_Path) as csv_file:
        csv_str=csv_file.read()
        csv_file.close()
        csv_str=csv_str.replace("    ",",")
        csv_str=csv_str.replace("   ",",")
        print(csv_str)
        Cylindres_dic= csv.reader(csv_str, delimiter=",")
        map=[]
        i=0
        for row in Cylindres_dic:
            i+=1
            for val in row:
                print(val,end=",")
            print(len(row))
            #map.append(Cylindres(x=row[0],y=row[1],Type=row[2],Id=i))           
        
        return map
        
map=Input_Map("Map.csv")
for Cyl in map:
    print(Cyl)