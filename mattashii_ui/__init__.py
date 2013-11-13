__author__ = 'matthias'

from gi.repository import Gtk

import mattashii

def main():
    builder = Gtk.Builder()
    builder.add_from_file("UI.glade")
    window = builder.get_object("mattashii_main")
    window.show_all()
    Gtk.main()
    return window

if __name__ == "__main__":
    main()