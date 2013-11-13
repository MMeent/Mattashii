

import json

from argparse import ArgumentParser

import models
import view
import controllers

import get_object
import default

def main(inputFile, writeFile, precision, writeDTime):

    # Get the data

    data = controllers.open(inputFile)

    # Sets some variables

    gc = controllers.variables.set_gconst(data) # Gravitational Constant
    Objects = controllers.variables.set_objects(data) # Objects list
    dt = controllers.variables.set_dt(writeDTime) # Output time
    timeStep = controllers.variables.set_timeStep(precision) # Time step used in simulation
    time = 0. # Time simulation started

    # This part does the magic: the simulation happens here

    while dt >= time:
        time += timeStep
        Objects = controllers.simulate(Objects, timeStep, gc)

    # Print the data

    print json.dumps(Objects, sort_keys=True, indent=4, separators=(',', ':'))

    # Gets the proper write file

    fileString = view.getFileString(writeFile)

    # Write the data to the writefile

    view.write(Objects, fileString)

    #return the objects list

    return fileString

if __name__ == "__main__":

    # Argument parsing

    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="Set the input file. Default is Bodies.json", default="Bodies.json")
    parser.add_argument("-w", "--writefile", help="Set the output file. Default is next WriteOut.json file")
    parser.add_argument("-p", "--precision", type=float, help="Set the precision rate, in seconds. Default is one second", default=1.)
    parser.add_argument("-wdt","--writeDTime", type=int, help="Set the dt for the output data, in seconds. Default is one hour", default=3600)
    args = parser.parse_args()
    print "arguments: ", args

    main(args.input, args.writefile, args.precision, args.writeDTime)