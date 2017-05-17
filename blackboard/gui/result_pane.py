import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, Gdk  # noqa


class result_pane(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.orientation = Gtk.Orientation.VERTICAL
        self.spacing = 0
        self.init_lb_list()


    def add_label(self, txt_op, value):
        if Gdk.keyval_name(value.keyval) == 'Return':
            x = txt_op.get_cursor_locations()
            pos = x.strong.y / x.strong.height + 1
            lb = Gtk.Label(str(pos))
            self.lb_list.insert(pos, lb)
            self.add(lb)
            lb.show()
