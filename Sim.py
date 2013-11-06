#!/usr/bin/env python

import mattashii
import argparse

def main():
    # Argument parsing

    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="Set the input file. Default is Bodies.json", default="Bodies.json")
    parser.add_argument("-w", "--writefile", help="Set the output file. Default is next WriteOut.json file")
    parser.add_argument("-p", "--precision", type=float, help="Set the precision rate, in seconds. Default is one second", default=1.)
    parser.add_argument("-wdt","--writeDTime", type=int, help="Set the dt for the output data, in seconds. Default is one hour", default=3600)
    args = parser.parse_args()
    print "arguments: ", args

    mattashii.main(args.input, args.writefile, args.precision, args.writeDTime)



if __name__ == '__main__':
    main()
