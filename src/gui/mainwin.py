import gi
from gi.repository import Gtk

gi.require_version('Gtk', '3.0')


class mainwin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(600, 400)
        self.connect('destroy', Gtk.main_quit)




win = mainwin()
win.show_all()
Gtk.main()
