__author__ = 'matthias'

from gi.repository import Gtk

def getSelected(treeview):
    """ This method gets the selected value from the given GTK treeview"""

    selection = treeview.get_selection()
    selection.set_mode(Gtk.SELECTION_SINGLE)
    tree_model, tree_iter = selection.get_selected()
    selected = tree_model.get_value(tree_iter, 0)
    return selected

def get_child_by_name(parent, childname):
    try:
        name = Gtk.Buildable.get_name
        for i in parent.get_children:
            if name(i) == childname:
                return i
    except:
        pass