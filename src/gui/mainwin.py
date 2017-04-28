import gi
from gi.repository import Gtk

gi.require_version('Gtk', '3.0')


class mainwin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(600, 400)
        self.connect('destroy', Gtk.main_quit)

        self.__add_scrolled_win()

    def __add_scrolled_win(self):
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_hexpand(True)
        self.scroll.set_vexpand(True)
        self.add(self.scroll)


win = mainwin()
win.show_all()
Gtk.main()
