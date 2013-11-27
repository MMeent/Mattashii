__author__ = 'matthias'

from gi.repository import Gtk

def get_input_from(item):
    pass
    if item is not None:
        pass
    else:
        return 0

def getSelected(tree_view):
    selection = tree_view.get_selection()
    selection.set_mode(Gtk.SELECTION_SINGLE)
    tree_model, tree_iter = selection.get_selected()
    selected = tree_model.get_value(tree_iter, 0)
    return selected
