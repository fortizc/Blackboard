import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio  # noqa


class result_pane(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.orientation = Gtk.Orientation.VERTICAL
        self.spacing = 0

    def add_label(self, txt_op, y):
        x = txt_op.get_cursor_locations()
        lb = Gtk.Label(str(x.strong.y))
        self.add(lb)
        lb.show()
