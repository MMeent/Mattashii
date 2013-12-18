__author__ = 'matthias'

from gi.repository import Gtk

def getSelected(treeview):
    """ This method gets the selected value from the given GTK treeview"""

    print type(treeview)
    try:
        selection = treeview.get_selection()
        tree_model, tree_iter = selection.get_selected()
        selected = tree_model.get_value(tree_iter, 0)
    except Exception as e:
        print e
        selected = None
    return selected

def get_child_by_name(parent, childname):
    try:
        name = Gtk.Buildable.get_name
        for i in parent.get_children():
            if name(i) == childname:
                return i
    except Exception as  e:
        print("problem found in checking " + parent + " for child " + childname + " : " + e)
        return None