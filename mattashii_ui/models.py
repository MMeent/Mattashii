__author__ = 'matthias'

from gi.repository import Gtk

import controllers
import view

def handlers():
    """This function returns the handlers to the connect to. """

    handlers = {
        "onDeleteWindow" : Gtk.main_quit,
        "on_Body1Treeview_select_cursor_row" : controllers.Update.TreeStores,
        "on_Body2Treeview_select_cursor_row" : controllers.Update.TreeStores,
        "on_PlotButton_clicked" : controllers.newSimulation.create,
    }

    return handlers