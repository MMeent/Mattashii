__author__ = 'mattashii'

from gi.repository import Gtk
from os import rename

import mattashii

import view as view

class Update(object):
    """This is the class created to contain the update methods, so that I can update the different things
    that i have to update"""

    @staticmethod
    def TreeStores(window):
        """The method to update the treestores in the window. """
        pass


    @staticmethod
    def Plot(window):
        """The method to update the plot. """
        pass

class newSimulation(object):
    """This is the class whose function it is to contain the methods for a new simulation, as the name suggests."""

    @staticmethod
    def create(Box):
        """This method has the possibilities to create a new simulation. The box in what the data are has to be given
        as an argument. Different steps are being saved with the .step(n) postfix. The last step is renamed to the
        original output filename. """

        Items = Box.get_children()
        for i in Items:
            for j in i:
                name = Gtk.Buildable.get_name(j)
                if name == "FileChosen":
                    InFile = j.get_filename()
                elif name == "OutFile":
                    OriginalOutFile = OutFileName = j.get_text()
                elif name == "PrecisionSlide":
                    precision = j.get_value()
                elif name == "TimePlot":
                    TimePlot = j.get_value() * 3600
                elif name == "StepsSlide":
                    Steps = j.get_value()

        if OutFileName is "NoneType":
            OriginalOutFile = OutFileName = "mattashii/Bodies.json"
        if (InFile == "NoneType") or (InFile is None):
            InFile == "mattashii/Bodies.json"

        print InFile, OutFileName, precision, TimePlot, Steps
        WriteDTime = TimePlot / Steps
        InFileName = InFile

        OutFileName = OutFileName + ".step1"
        with open(mattashii.main(InFileName, OutFileName, precision, WriteDTime)) as data:
            NewPlot = newSimulation.Plot(data, plot=None)

        for i in range(int(Steps)):
            print i
            InFileName = OutFileName
            OutFileName = OriginalOutFile + ".step" + str(i + 1)
            with open(mattashii.main(InFileName, OutFileName, precision, WriteDTime)) as data:
                NewPlot = newSimulation.Plot(data, plot=None)

        rename(OutFileName, OriginalOutFile)

    @staticmethod
    def Plot(data, plot):
        """This method creates a new plot for the plot window."""
        NewWindow = Update.Plot(plot)
        return NewWindow
