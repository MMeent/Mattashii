__author__ = 'matthias'

import math
import view
import models

def simulate(objects, dt, Gc):
    for obj in objects:
        body.reset_acceleration(obj)
        for object in objects:
            body.accelerate(obj, object, Gc)
    for obj in objects:
        body.update(obj, dt)
    return objects

class body (object):
    @staticmethod
    def update(object, dt):
        object["x"] += object["vx"]*dt
        object["y"] += object["vy"]*dt
        object["z"] += object["vz"]*dt
        object["vx"] += object["ax"]*dt
        object["vy"] += object["ay"]*dt
        object["vz"] += object["az"]*dt
        object["ax"], object["ay"], object["az"] = 0., 0., 0.

    @staticmethod
    def accelerate(obj, object, Gc):
        force = view.force(obj, object, Gc)
        distance = view.distance(obj, object)
        if distance != 0:
            obj["ax"] += force*(obj["x"] - object["x"])/distance
            obj["ay"] += force*(obj["y"] - object["y"])/distance
            obj["az"] += force*(obj["z"] - object["z"])/distance

    @staticmethod
    def reset_acceleration(obj):
        obj["ax"], obj["ay"], obj["az"] = 0., 0., 0.