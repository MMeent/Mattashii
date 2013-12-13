__author__ = 'matthias'

from gi.repository import Gtk

def getSelected(tree_view):
    """ This method gets the selected value from the given GTK treeview"""

    selection = tree_view.get_selection()
    selection.set_mode(Gtk.SELECTION_SINGLE)
    tree_model, tree_iter = selection.get_selected()
    selected = tree_model.get_value(tree_iter, 0)
    return selected
