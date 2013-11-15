__author__ = 'matthias'

from gi.repository import Gtk

import mattashii

import models
import view
import controllers


def main():
    builder = Gtk.Builder()
    builder.add_from_file("UI.glade")

    handlers = models.handlers()
    builder.connect_signals(handlers)
    window = builder.get_object("mattashii_main")
    window.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()