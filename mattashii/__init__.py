import json
import models
import controllers
import view
import get_object
import default
import argparse
import os


def main(inputFile, writeFile, precision, writeDTime):

    # Input file processing
    if inputFile != None:
        with open(inputFile, 'r') as f:
            data = json.load(f)
        print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
    else:
        data = {"Help": "None"}
        print "No input filename given. Using this data instead: {data}".format(data=data)

    # Sets gravitational constant from imported file for calculations

    try:
        GravityConstant = gc = data["GravityConstant"]
    except:
        print "No gravitational constant included in input file. Using default instead. ({GC})".format(GC=default.GravityConstant())
        GravityConstant = gc = default.GravityConstant()

    print "Gravitational Constant: {Gc}".format(Gc = GravityConstant)

    # Sets some variables

    try:
        Objects = data["Objects"]
    except:
        print "No objects included in input file. Using default list instead."
        Objects = default.Objects()

    try:
        dt = float(writeDTime)
    except:
        dt = default.writeDTime()
        print "No write time found. Using default instead. ({delta})".format(delta=dt)

    try:
        timeStep = float(precision)
    except:
        timeStep = default.timeStep()
        print "No precision found. Using default instead. ({pr})".format(pr=timeStep)

    time = 0.

    # This part does the magic: the simulation happens here

    while dt >= time:
        time += timeStep
        Objects = controllers.simulate(Objects, timeStep, gc)

    # Print the data

    print json.dumps(Objects, sort_keys=True, indent=4, separators=(',', ':'))

    # Gets the proper write file

    found = False
    if not(writeFile == None):
        found = True
        fileString = writeFile
    fileNo = 1
    while found != True:
        fileString = "WriteOut" + str(fileNo) + ".json"
        if not(os.path.isfile(fileString)):
            found = True
        else:
            fileNo += 1

    # Write the data to the writefile

    try:
        with open(fileString, "w") as outfile:
            json.dump(Objects, outfile)
    except:
        print "problems with writing to file named \"{file}\"".format(file = fileString)

if __name__ == "__main__":

    # Argument parsing

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Set the input file. Default is Bodies.json", default="Bodies.json")
    parser.add_argument("-w", "--writefile", help="Set the output file. Default is next WriteOut.json file")
    parser.add_argument("-p", "--precision", type=float, help="Set the precision rate, in seconds. Default is one second", default=1.)
    parser.add_argument("-wdt","--writeDTime", type=int, help="Set the dt for the output data, in seconds. Default is one hour", default=3600)
    args = parser.parse_args()
    print "arguments: ", args

    main(args.input, args.writefile, args.precision, args.writeDTime)