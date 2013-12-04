__author__ = 'matthias'

from gi.repository import Gtk
from os import rename

import mattashii

import view as view

class Update(object):
    @staticmethod
    def TreeStores(window):
        pass
        go = window.get_object
        Body1 = view.getSelected(go("Body1Treeview"))
        Body2 = view.getSelected(go("Body2Treeview"))


    @staticmethod
    def Plot(window):
        pass

class newSimulation(object):
    @staticmethod
    def create(Box):
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

        print type(OutFileName)
        print type(InFile)


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
        NewWindow = Update.Plot(plot)
        return NewWindow
