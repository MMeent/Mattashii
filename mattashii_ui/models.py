__author__ = 'matthias'

from gi.repository import Gtk

import controllers
import view

def handlers():
    return {
        "onDeleteWindow" : Gtk.main_quit,
        "on_Body1Treeview_select_cursor_row" : controllers.Update.TreeStores,
        "on_Body2Treeview_select_cursor_row" : controllers.Update.TreeStores,
    }