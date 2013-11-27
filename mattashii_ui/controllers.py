__author__ = 'matthias'

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
    def create(Window):
        with open(mattashii.main(None, None, None, None)) as data:
            NewWindow= newSimulation.Plot(data, Window)

    @staticmethod
    def Plot(data, plot):
        pass
        NewWindow = Update.Plot(plot)
        return NewWindow
