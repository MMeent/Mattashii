#!/usr/bin/env python

from argparse import ArgumentParser

import mattashii
import mattashii_ui

def main():
    # Argument parsing

    parser = ArgumentParser()
    parser.add_argument("-i", "--input", help="Set the input file. Default is Bodies.json", default="Bodies.json")
    parser.add_argument("-w", "--writefile", help="Set the output file. Default is next WriteOut.json file")
    parser.add_argument("-p", "--precision", type=float, help="Set the precision rate, in seconds. Default is one second", default=1.)
    parser.add_argument("-wdt","--writeDTime", type=int, help="Set the dt for the output data, in seconds. Default is one hour", default=3600)
    parser.add_argument("-ng", "--nogui", help="No graphical user interface, just simulate the f*ck out of here", default=False, action="store_true")
    args = parser.parse_args()
    print "arguments: ", args

    if args.nogui == False:
        window = mattashii_ui.main()
    else:
        mattashii.main(args.input, args.writefile, args.precision, args.writeDTime)



if __name__ == '__main__':
    main()
