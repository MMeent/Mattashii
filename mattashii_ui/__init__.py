__author__ = 'matthias'

from gi.repository import Gtk

import mattashii

import models
import view
import controllers


def main():
    """This is the main() for mattashii_ui, where galaxies are plotted using a gui. It first loads the UI.glade from
    the mattashii_ui folder, then connects the signals from the models.py, and lastly builds the main window."""

    builder = Gtk.Builder()
    builder.add_from_file("mattashii_ui/UI.glade")

    handlers = models.handlers()
    builder.connect_signals(handlers)

    window = builder.get_object("mattashii_main")
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()