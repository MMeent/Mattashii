__author__ = 'matthias'

from gi.repository import Gtk

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
                print name
                print type(j)
                if name == "FileChosen":
                    InFile = j.get_filename()
                elif name == "OutFile":
                    OutFileName = j.get_text()
                elif name == "PrecisionSlide":
                    precision = j.get_value()
                elif name == "TimePlot":
                    TimePlot = j.get_value()
                elif name == "StepsSlide":
                    Steps = int(j.get_value())
        if OutFileName == None:
            OutFileName = "Bodies"
        if InFile == None:
            InFile == "Bodies.json"
        print InFile, OutFileName, precision, TimePlot, Steps
        WriteDTime = TimePlot / Steps
        for i in range(Steps):
            InFileName = InFile + i + ".json"
            with open(mattashii.main(InFileName, OutFileName, precision, WriteDTime)) as data:
                NewPlot = newSimulation.Plot(data, plot)

    @staticmethod
    def Plot(data, plot):
        NewWindow = Update.Plot(plot)
        return NewWindow
