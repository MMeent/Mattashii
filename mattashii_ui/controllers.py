__author__ = 'mattashii'

from gi.repository import Gtk
from os import rename
from multiprocessing import Process

import mattashii
from mattashii import default

import view

from models import Set

class Update(object):
    """ This is the class created to contain the update methods, so that I can update the different things
    that i have to update"""

    @staticmethod
    def Boxes(InfoBox, widget):
        """ The method to update the Liststores in the window. """
        name = Gtk.Buildable.get_name
        child = view.get_child_by_name
        data = default.Objects()
        print "hello"
        try:
            b1box = child(InfoBox, "Body 1 box")
            b1info = child(b1box, "Body1info")
            b1treeview = child(b1info, "Body1Treeview")
            b1treeview = Set.BodyTreeview(b1treeview, data)
            b1selection = view.getSelected(b1treeview)
            b1hbox = child(b1info, "B1HBox")
            b1info = child(b1hbox, "B1VBox2")
            b1name = child(b1info, "B1Name")
            b1type = child(b1info, "B1Type")
            b1mass = child(b1info, "B1Mass")
            b1radius = child(b1info, "B1Radius")
            b1surtemp = child(b1info, "B1SurTemp")
            b1surpre = child(b1info, "B1SurPre")
            print "box 1 done"


            b2box = child(InfoBox, "Body 2 box")
            b2info = child(b2box, "Body2info")
            b2treeview = child(b2info, "Body2Treeview")
            b2treeview = Set.BodyTreeview(b2treeview, data)
            b2selection = view.getSelected(b2treeview)
            b2hbox = child(b2info, "B2HBox")
            b2info = child(b2hbox, "B2VBox2")
            b2name = child(b2info, "B2Name")
            b2type = child(b2info, "B2Type")
            b2mass = child(b2info, "B2Mass")
            b2radius = child(b2info, "B2Radius")
            b2surtemp = child(b2info, "B2SurTemp")
            b2surpre = child(b2info, "B2SurPre")
            print "box 2 done"

            dbbox = child(InfoBox, "DifferenceBox")
            dbinfo = child(dbbox, "DBox")
            dbdata = child(dbinfo, "Data")
            dbmass = child(dbdata, "deltaMass")
            dbradius = child(dbdata, "deltaRadius")
            dbsurtemp = child(dbdata, "deltaSurfaceTemperature")
            dbpre = child(dbdata, "deltaPressure")
            dbdist = child(dbdata, "deltaDistance")
            dbsign = child(dbdata, "deltaSignal")
            print "difference done"


        except:
            print "didn't work"

    @staticmethod
    def Plot(window):
        """ The method to update the plot. """
        pass

class newSimulation(object):
    """ This is the class whose function it is to contain the methods for a new simulation, as the name suggests."""

    @staticmethod
    def Create(Box):
        """ This method has the possibilities to create a new simulation. The box in what the data are has to be given
        as an argument. Different steps are being saved with the .step(n) postfix. The last step is renamed to the
        original output filename. """

        # get the plot info box
        Notebook = Box.get_parent()
        for i in Notebook.get_children():
            name = Gtk.Buildable.get_name(i)
            if name == "PlotInfoBox":
                OtherBox = i

        # get the input data
        Items = Box.get_children()
        for i in Items:
            for j in i:
                name = Gtk.Buildable.get_name(j)
                if name == "FileChosen":
                    InFile = j.get_filename()
                elif name == "OutFile":
                    OriginalOutFile = OutFileName = j.get_text()
                elif name == "PrecisionSlide":
                    Precision = j.get_value()
                elif name == "TimePlot":
                    TimePlot = j.get_value() * 3600
                elif name == "StepsSlide":
                    Steps = j.get_value()

        # correct errors
        if OutFileName is "NoneType":
            OriginalOutFile = OutFileName = "mattashii/Bodies.json"
        if (InFile == "NoneType") or (InFile is None):
            InFile == "mattashii/Bodies.json"

        Items = OtherBox.get_children()
        for i in Items:
            name = Gtk.Buildable.get_name
            iName = name(i)
            try:
                childs = i.get_children()
                if iName == "File":
                    for k in childs:
                        if name(k) == "Fvalue":
                            k.set_text(InFile)
                elif iName == "Time":
                    for k in childs:
                        if name(k) == "Tvalue":
                            k.set_text(str(TimePlot/3600))
                elif iName == "Precision":
                    for k in childs:
                        if name(k) == "Pvalue":
                            k.set_text(str(Precision))
                elif iName == "Steps":
                    for k in childs:
                        if name(k) == "Svalue":
                            k.set_text(str(Steps))
            except:
                pass

        # debug
        print InFile, OutFileName, Precision, TimePlot, Steps
        WriteDTime = TimePlot / Steps
        InFileName = InFile

        process = Process(target=newSimulation.Simulate, args=(InFileName, OriginalOutFile, OutFileName, Precision, WriteDTime, Steps))
        process.start()

    @staticmethod
    def Plot(data, plot):
        """ This method creates a new plot for the plot window."""
        NewWindow = Update.Plot(plot)
        return NewWindow

    @staticmethod
    def Simulate(InFileName, OriginalOutFile, OutFileName, Precision, WriteDTime, Steps):
        OutFileName = OutFileName + ".step1"
        with open(mattashii.main(InFileName, OutFileName, Precision, WriteDTime)) as data:
            NewPlot = newSimulation.Plot(data, plot=None)

        # loop through steps
        for i in range(int(Steps)):
            print i
            InFileName = OutFileName
            OutFileName = OriginalOutFile + ".step" + str(i + 1)
            with open(mattashii.main(InFileName, OutFileName, Precision, WriteDTime)) as data:
                NewPlot = newSimulation.Plot(data, plot=None)

        rename(OutFileName, OriginalOutFile)
        print "I'm done processing"