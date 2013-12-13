__author__ = 'matthias'

from gi.repository import Gtk

import controllers
import view

def handlers():
    """ This function returns the handlers to the connect to. """

    handlers = {
        "onDeleteWindow" : Gtk.main_quit,
        "on_Body1Listview_select_cursor_row" : controllers.Update.Boxes,
        "on_Body2Listview_select_cursor_row" : controllers.Update.Boxes,
        "on_PlotButton_clicked" : controllers.newSimulation.Create,
        "on_mattashii_main_set_focus" : controllers.Update.Boxes,
    }

    return handlers