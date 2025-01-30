import math
from Cylindres import *
from Robot import *

def sign(x):
    return -1 if x < 0 else 1

def intersectSegmentCircleP(robot, cylindre, cylindre2):
    r = cylindre2.Rayon
    x1 = cylindre.x - cylindre2.x
    y1 = cylindre.y - cylindre2.y
    x2 = robot.x - cylindre2.x
    y2 = robot.y - cylindre2.y
    dx = x2 - x1
    dy = y2 - y1
    dr = math.sqrt(dx * dx + dy * dy)
    D = x1 * y2 - x2 * y1
    discriminant = r * r * dr * dr - D * D

    if discriminant < 0:
        return (None,None),(None,None)
    if discriminant == 0:
        return ((D * dy) / (dr * dr) + cylindre2.x, (-D * dx) / (dr * dr) + cylindre2.y)
    
    discriminant = math.sqrt(discriminant)
    xa = (D * dy + sign(dy) * dx * discriminant) / (dr * dr)
    xb = (D * dy - sign(dy) * dx * discriminant) / (dr * dr)
    ya = (-D * dx + abs(dy) * discriminant) / (dr * dr)
    yb = (-D * dx - abs(dy) * discriminant) / (dr * dr)
    
    return (xa + cylindre2.x, ya + cylindre2.y), (xb + cylindre2.x, yb + cylindre2.y)

def intersectSegmentCircle(robot, cylindre, cylindre2):
    (x1, y1), (x2, y2) = intersectSegmentCircleP(robot, cylindre, cylindre2)
    if x1 is None or y1 is None or x2 is None or y2 is None:
        return False

    def is_between(a, b, c):
        return min(a, b) <= c <= max(a, b)

    return (is_between(robot.x, cylindre.x, x1) and is_between(robot.y, cylindre.y, y1)) or \
           (is_between(robot.x, cylindre.x, x2) and is_between(robot.y, cylindre.y, y2))

def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)

# Return true if line segments AB and CD intersect
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)