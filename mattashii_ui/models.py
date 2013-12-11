__author__ = 'matthias'

from gi.repository import Gtk

import controllers
import view

def handlers():
    """This function returns the handlers to the connect to. """

    handlers = {
        "onDeleteWindow" : Gtk.main_quit,
        "on_Body1Listview_select_cursor_row" : controllers.Update.ListStores,
        "on_Body2Listview_select_cursor_row" : controllers.Update.ListStores,
        "on_PlotButton_clicked" : controllers.newSimulation.Create,
    }

    return handlers