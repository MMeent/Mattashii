__author__ = 'matthias'

import json
import os

import view
import models
import default

def openJson(inputFile):
    """ Opens the json file with filename 'inputFile'. If none, it'll use the default instead. """
    if inputFile is not None:
        with open(inputFile, 'r') as f:
            data = json.load(f)
        print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
    else:
        data = default.data()
        print "No input filename given. Using this data instead: {data}".format(data=data)
    return data

def simulate(objects, dt, Gc):
    """ Simulates the universe. No, just kidding, but it's very close: the objects given will be simulated by this
    function. """
    for obj in objects:
        body.reset_acceleration(obj)
        for object in objects:
            body.accelerate(obj, object, Gc)
    for obj in objects:
        body.update(obj, dt)
    return objects

def simulateObject(object, objects, Gc):
    body.reset_acceleration(object)
    for obj in objects:
        body.accelerate(object, obj, Gc)


class variables(object):
    """ Collects all the set_*-objects to make my code more readable. """

    @staticmethod
    def set_gconst(data):
        """ Sets the gravity constant from the data given. If none, it'll use the default instead. """
        try:
            gc = data["GravityConstant"]
        except:
            gc = default.GravityConstant()
            print "No gravitational constant included in input file. Using default instead. ({GC})".format(GC=gc)
        return gc

    @staticmethod
    def set_objects(data):
        """ Gets the list of objects from the data given. If none, it'll use the default instead. """
        try:
            Objects = data["Objects"]
        except:
            print "No objects included in input file. Using default list instead."
            Objects = default.Objects()
        return Objects

    @staticmethod
    def set_dt(data):
        """ Returns the difference in time to do the calculations in before it'll be written to a file. If none, it'll
        use the default instead. """
        try:
            dt = float(data)
        except:
            dt = default.writeDTime()
            print "No write time found. Using default instead. ({delta})".format(delta=dt)
        return dt

    @staticmethod
    def set_timeStep(data):
        """ Returns the difference in time to simulate every step. If none, it'll use the default instead. """
        try:
            timeStep = float(data)
        except:
            timeStep = default.timeStep()
            print "No precision found. Using default instead. ({pr})".format(pr=timeStep)
        return timeStep

class body (object):
    """ Contains some functions used on the different celestial objects """

    @staticmethod
    def update(object, dt):
        """ Applies the calculated velocity to it's place, and then it's acceleration to it's velocity. """
        object["x"] += object["vx"]*dt
        object["y"] += object["vy"]*dt
        object["z"] += object["vz"]*dt
        object["vx"] += object["ax"]*dt
        object["vy"] += object["ay"]*dt
        object["vz"] += object["az"]*dt
        object["ax"], object["ay"], object["az"] = 0., 0., 0.

    @staticmethod
    def accelerate(obj, object, Gc):
        """ Calculates the acceleration of an object to another object, when the distance is not equal to 0. """
        force = view.force(obj, object, Gc)
        distance = view.distance(obj, object)
        if distance != 0:
            obj["ax"] += force*(obj["x"] - object["x"])/distance
            obj["ay"] += force*(obj["y"] - object["y"])/distance
            obj["az"] += force*(obj["z"] - object["z"])/distance

    @staticmethod
    def reset_acceleration(obj):
        """ Resets the acceleration to it's default state of 0. """
        obj["ax"], obj["ay"], obj["az"] = 0., 0., 0.