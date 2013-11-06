import math
import controllers
import json

def getFileString(writeFileString):
    """ Gets the write file file string. If none, it'll calculate the next write file file string. """
    fileString = ""
    found = False

    if writeFileString is not None:
        found = True
        fileString = writeFileString

    fileNo = 1
    while found != True:
        fileString = "WriteOut" + str(fileNo) + ".json"
        if not(os.path.isfile(fileString)):
            found = True
        else:
            fileNo += 1
    return fileString

def force(obj, object, Gc):
    """ Calculates the force between two objects, by using the two masses, and the gravity constant.
    If distance is 0, it'll return 0. """
    delta = distance(obj, object)
    if delta != 0:
        force = Gc * obj["mass"] * object["mass"] / (delta*delta)
    else:
        force = 0
    return force

def distance(obj, object):
    """ Calculates the absolute distance between two objects. """
    dx = obj["x"] - object["x"]
    dy = obj["y"] - object["y"]
    dz = obj["z"] - object["z"]
    return math.sqrt(dx**2 + dy**2 + dz **2)


def write(data, file):
    """ Writes the data to a file, if possible. """
    try:
        with open(file, "w") as outfile:
            json.dump(data, outfile)
    except:
        print " Problems with writing to file named \"{file}\" \n No write performed".format(file = file)

