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
    
    jsonStars = data["Stars"]
    jsonPlanets = data["Planets"]
    jsonMoons = data["Moons"]
    jsonAstroids = data["Astroids"]
    jsonSatellites = data["Satellites"]
    print "Stars: {data}".format(data = jsonStars)
    print "Planets: {data}".format(data = jsonPlanets)
    print "Moons: {data}".format(data = jsonMoons)
    print "Astroids: {data}".format(data = jsonAstroids)
    print "Satellites: {data}".format(data = jsonSatellites)
    
    

if __name__ == '__main__':
    main()
