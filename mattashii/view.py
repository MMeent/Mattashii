import math
import controllers


def force(obj, object, Gc):
    delta = distance(obj, object)
    if delta != 0:
        force = Gc * obj["mass"] * object["mass"] / (delta*delta)
    else:
        force = 0
    return force

def distance(obj, object):
    dx = obj["x"] - object["x"]
    dy = obj["y"] - object["y"]
    dz = obj["z"] - object["z"]
    return math.sqrt(dx**2 + dy**2 + dz **2)

