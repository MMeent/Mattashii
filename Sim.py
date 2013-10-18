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
        stars.append(GBodies.Star.deserialize(star))

    planets = []
    jsonPlanets = data["Planets"]
    print "Planets: {data}".format(data = jsonPlanets)
    for planet in jsonPlanets:
        planets.append(GBodies.Planet.deserialize(planet))

    moons = []
    jsonMoons = data["Moons"]
    print "Moons: {data}".format(data = jsonMoons)
    for moon in jsonMoons:
        moons.append(GBodies.Moon.deserialize(moon))

    astroids = []
    jsonAstroids = data["Astroids"]
    print "Astroids: {data}".format(data = jsonAstroids)
    for astroid in jsonAstroids:
        astroids.append(GBodies.Astroid.deserialize(astroid))

    satellites = []
    jsonSatellites = data["Satellites"]
    print "Satellites: {data}".format(data = jsonSatellites)
    for satellite in jsonSatellites:
        satellites.append(GBodies.Satellite.deserialize(satellite))



    stardata = []
    moondata = []
    plandata = []
    astrdata = []
    satedata = []
    for star in stars:
        stardata.append(star.serialize())
    for moon in moons:
        moondata.append(moon.serialize())
    for planet in planets:
        plandata.append(planet.serialize())
    for astroid in astroids:
        astrdata.append(astroid.serialize())
    for satellite in satellites:
        satedata.append(satellite.serialize())
    AllBodies = { "stars" : stardata,
                  "moons" : moondata,
                  "planets" : plandata,
                  "astroids" : astrdata,
                  "satellites" : satedata,
                  }
    print AllBodies

    print "data: ", json.dumps(AllBodies)

if __name__ == '__main__':
    main()
