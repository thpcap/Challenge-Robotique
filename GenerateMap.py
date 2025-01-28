import random

def distance(ax, ay, bx, by):
    return ((ax-bx)**2 + (ay-by)**2)**0.5

def generateMap(cylinder_number, x_max, y_max, x_min, y_min, distance_threshold):
    cylinder_list = []
    for i in range(cylinder_number):
        flag = True
        count = 0
        while flag:
            # limit the number of iteration in case the result is not achievable
            count += 1
            if count > 10000:
                return cylinder_list

            flag = False

            # Generate coordinates and test if it is not too close to another cylinder
            temp_x = random.random() * x_max + x_min
            temp_y = random.random() * y_max + y_min
            for j in range(len(cylinder_list)):
                if distance(cylinder_list[j][0], cylinder_list[j][1], temp_x, temp_y) < distance_threshold:
                    flag = True
        cylinder_list.append((temp_x, temp_y, float(int(random.random() * 3 + 1))))
    return cylinder_list

def writeMap(cylinder_list):
    f = open("random_map.csv", "w")
    f.write("")
    f.close()

    f = open("random_map.csv",mode="a")
    for cylinder in cylinder_list:
        f.write(str(cylinder[0]) + "    " + str(cylinder[1]) + "    " + str(cylinder[2]) + "\n")
    f.close()

def generate(cylinder_number, x_max = 25, y_max = 20, x_min = 0, y_min = 0, distance_threshold = 1):
    writeMap(generateMap(cylinder_number, x_max, y_max, x_min, y_min, distance_threshold))

generate(20)