#!/usr/bin/env python

import sys
import math
import json
import GBodies

def main():
    with open('Bodies.json', 'r') as f:
        data = json.load(f)

    print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
    
    GravityConstant = data["GravityConstant"]
    print "Gravitational Constant: {gc}".format(gc = GravityConstant)
    
    stars = []
    jsonStars = data["Stars"]
    print "Stars: {data}".format(data = jsonStars)
    for star in jsonStars:
        bdata = star["body"]
        spdata = bdata["SpatialData"]
        stars.append(GBodies.Star(
            spdata["x"], 
            spdata["y"], 
            spdata["z"], 
            spdata["vx"],
            spdata["vy"],
            spdata["vz"],
            bdata["mass"],
            bdata["radius"],
            star["name"]))
    planets = []
    jsonPlanets = data["Planets"]
    print "Planets: {data}".format(data = jsonPlanets)
    for planet in jsonPlanets:
        bdata = planet["body"]
        spdata = bdata["SpatialData"]
        planets.append(GBodies.Planet(
            spdata["x"],
            spdata["y"],
            spdata["z"],
            spdata["vx"],
            spdata["vy"],
            spdata["vz"],
            bdata["mass"],
            bdata["radius"],
            planet["SurfacePressure"],
            planet["name"]))

    moons = []
    jsonMoons = data["Moons"]
    print "Moons: {data}".format(data = jsonMoons)
    for moon in jsonMoons:
        bdata = moon["body"]
        spdata = bdata["SpatialData"]
        moons.append(GBodies.Moon(
            spdata["x"],
            spdata["y"],
            spdata["z"],
            spdata["vx"],
            spdata["vy"],
            spdata["vz"],
            bdata["mass"],
            bdata["radius"],
            moon["SurfacePressure"],
            moon["name"]))

    astroids = []
    jsonAstroids = data["Astroids"]
    print "Astroids: {data}".format(data = jsonAstroids)
    for astroid in jsonAstroids:
        bdata = astroid["body"]
        spdata = bdata["SpatialData"]
        astroids.append(GBodies.Astroid(
            spdata["x"],
            spdata["y"],
            spdata["z"],
            spdata["vx"],
            spdata["vy"],
            spdata["vz"],
            bdata["mass"],
            bdata["radius"],
            astroid["name"]))

    satellites = []
    jsonSatellites = data["Satellites"]
    print "Satellites: {data}".format(data = jsonSatellites)
    for satellite in jsonSatellites:
        bdata = satellite["body"]
        spdata = satellite["SpatialData"]
        satellite.append(GBodies.Satellite(
            spdata["x"],
            spdata["y"],
            spdata["z"],
            spdata["vx"],
            spdata["vy"],
            spdata["vz"],
            bdata["mass"],
            satellite["name"]))


if __name__ == '__main__':
    main()
