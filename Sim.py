#!/usr/bin/env python

import sys
import math
import argparse
import os.path
import json
import GBodies

def Simulate(data, time, GravityConstant):
    stars = data["stars"]
    planets = data["planets"]
    moons = data["moons"]
    asteroids = data["asteroids"]
    satellites = data["satellites"]
    for star in stars:
        for starlevel2 in stars:
            star.accelerate(starlevel2, GravityConstant)

        for planetlevel2 in planets:
            star.accelerate(planetlevel2, GravityConstant)
            planetlevel2.accelerate(star, GravityConstant)

        for moonlevel2 in moons:
            star.accelerate(moonlevel2, GravityConstant)
            moonlevel2.accelerate(star, GravityConstant)

        for asteroidlevel2 in asteroids:
            star.accelerate(asteroidlevel2, GravityConstant)
            asteroidlevel2.accelerate(star, GravityConstant)

        for satellitelevel2 in satellites:
            star.accelerate(satellitelevel2, GravityConstant)
            satellitelevel2.accelerate(star, GravityConstant)

    for planet in planets:
        for planetlevel2 in planets:
            planet.accelerate(planetlevel2, GravityConstant)

        for moonlevel2 in moons:
            planet.accelerate(moonlevel2, GravityConstant)
            moonlevel2.accelerate(planet, GravityConstant)

        for asteroidlevel2 in aseteroids:
            planet.accelerate(asteroidlevel2, GravityConstant)
            asteroidlevel2.accelerate(planet, GravityConstant)

        for satellitelevel2 in satellites:
            planet.accelerate(satellitelevel2, GravityConstant)
            satellitelevel2.accelerate(planet, GravityConstant)

    for moon in moons:
        for moonlevel2 in moons:
            moon.accelerate(moonlevel2, GravityConstant)

        for asteroidlevel2 in asteroids:
            moon.accelerate(asteroidlevel2, GravityConstant)
            asteroidlevel2.accelerate(moon, GravityConstant)

        for satellitelevel2 in satellites:
            moon.accelerate(satellitelevel2, GravityConstant)
            satellitelevel2.accelerate(moon, GravityConstant)

    for asteroid in asteroids:
        for asteroidlevel2 in asteroids:
            asteroid.accelerate(asteroidlevel2, GravityConstant)

        for satellitelevel2 in satellites:
            asteroid.accelerate(satellitelevel2, GravityConstant)
            satellitelevel2.accelerate(asteroid, GravityConstant)

    for satellite in satellites:
        for satellitelevel2 in satellites:
            satellite.accelerate(satellitelevel2, GravityConstant)

    for star in stars:
        star.update()
    for planet in planets:
        planet.update()
    for moon in moons:
        moon.update()
    for asteroid in asteroids:
        asteroid.update()
    for satellite in satellites:
        satellite.update()

    data = { "stars" : stars,
             "planets" : planets,
             "moons" : moons,
             "asteroids" : asteroids,
             "satellites" : satellites,
            }

    return data


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Set the input file. Default is Bodies.json", default="Bodies.json")
    parser.add_argument("-w", "--writefile", help="Set the output file. Default is next WriteOut.json file")
    parser.add_argument("-p", "--precision", type=float, help="Set the precision rate, in seconds. Default is one second", default=1.)
    parser.add_argument("-wdt","--writeDtime", type=int, help="Set the dt for the output data, in seconds. Default is one hour", default=3600)
    args = parser.parse_args()
    print "arguments: ", args

    input = args.input

    with open(input, 'r') as f:
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

    asteroids = []
    jsonasteroids = data["Asteroids"]
    print "asteroids: {data}".format(data = jsonasteroids)
    for asteroid in jsonasteroids:
        asteroids.append(GBodies.Asteroid.deserialize(asteroid))

    satellites = []
    jsonSatellites = data["Satellites"]
    print "Satellites: {data}".format(data = jsonSatellites)
    for satellite in jsonSatellites:
        satellites.append(GBodies.Satellite.deserialize(satellite))

    data = { "stars" : stars,
             "planets" : planets,
             "moons" : moons,
             "asteroids" : asteroids,
             "satellites" : satellites,
            }

    dt = float(args.writedtime)
    time = 0.
    timestep = args.precision
    while dt >= time:
        time += timestep
        Simulate(data, timestep, GravityConstant)




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
    for asteroid in asteroids:
        astrdata.append(asteroid.serialize())
    for satellite in satellites:
        satedata.append(satellite.serialize())
    AllBodies = { "stars" : stardata,
                  "moons" : moondata,
                  "planets" : plandata,
                  "asteroids" : astrdata,
                  "satellites" : satedata,
                  }
    print AllBodies

    print "data: ", json.dumps(AllBodies)

    found = False
    if not(args.writefile == None):
        found = True
        filestring = args.writefile
    fileNo = 1
    while found != True:
        filestring = "WriteOut" + str(fileNo) + ".json"
        if not(os.path.isfile(string)):
            found = True
        else:
            fileNo += 1

    with open(filestring, "w") as outfile:
        json.dump(AllBodies, outfile)


if __name__ == '__main__':
    main()
