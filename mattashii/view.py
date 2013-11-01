import math
import controllers


@staticmethod
def force(obj, object, Gc):
    delta = Body.distance(obj, object)
    force = Gc * obj["mass"] * object["mass"] / (delta*delta)
    return force

@staticmethod
def distance(obj, object):
    dx = obj["x"] - object["x"]
    dy = obj["y"] - object["y"]
    dz = obj["z"] - object["z"]
    return math.sqrt(dx**2 + dy**2 + dz **2)