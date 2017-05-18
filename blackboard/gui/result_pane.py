import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, Gdk  # noqa


class result_pane(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.__init_lb_list()

    def __init_lb_list(self):
        lb = Gtk.Label(str(0))
        self.lb_list = []
        self.lb_list.append(lb)
        self.attach(lb, 0, 0, 100, 20)
        lb.show()

    def add_label(self, txt_op, value):
        if Gdk.keyval_name(value.keyval) == 'Return':
            x = txt_op.get_cursor_locations()
            pos = x.strong.y + x.strong.height
            index = pos / x.strong.height
            lb = Gtk.Label(str(index))
            self.lb_list.insert(index, lb)
            self.attach(lb, 0, pos, 100, x.strong.height)
            lb.show()
