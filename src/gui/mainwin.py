from gi.repository import Gtk


class mainwin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(600, 400)
        self.connect('destroy', Gtk.main_quit)
        self.show_all()


mainwin()
Gtk.main()
