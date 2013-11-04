__author__ = 'matthias'

import json
import models
import controllers
import view
import get_object
import argparse
import os


def main():
    pass

    # Argument parsing

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Set the input file. Default is Bodies.json", default="Bodies.json")
    parser.add_argument("-w", "--writefile", help="Set the output file. Default is next WriteOut.json file")
    parser.add_argument("-p", "--precision", type=float, help="Set the precision rate, in seconds. Default is one second", default=1.)
    parser.add_argument("-wdt","--writeDtime", type=int, help="Set the dt for the output data, in seconds. Default is one hour", default=3600)
    args = parser.parse_args()
    print "arguments: ", args

    # Input file processing

    with open(args.input, 'r') as f:
        data = json.load(f)
    print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))

    GravityConstant = gc = data["GravityConstant"]
    print "Gravitational Constant: {Gc}".format(Gc = GravityConstant)

    Objects = data["Objects"]

    dt = float(args.writeDtime)
    time = 0.
    timestep = args.precision
    while dt >= time:
        time += timestep
        Objects = controllers.simulate(Objects, timestep, gc)

    print Objects

    # Gets the proper write file

    found = False
    if not(args.writefile == None):
        found = True
        filestring = args.writefile
    fileNo = 1
    while found != True:
        filestring = "WriteOut" + str(fileNo) + ".json"
        if not(os.path.isfile(filestring)):
            found = True
        else:
            fileNo += 1

    with open(filestring, "w") as outfile:
        json.dump(Objects, outfile)

if __name__ == "__main__":
    main()