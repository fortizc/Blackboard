import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, Gdk  # noqa


class result_pane(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.lb_list = []
        self.__add_label(0)

    def __add_label(self, index):
        lb = Gtk.Label(str(index))
        self.lb_list.insert(index, lb)
        if (len(self.lb_list) - 1) > index:
            self.insert_row(index)
        self.attach(lb, 0, index, 1, 1)
        lb.show()

    def capture_pressed_key(self, txt_op, value):
        if Gdk.keyval_name(value.keyval) != 'Return':
            return
        x = txt_op.get_cursor_locations()
        height = x.strong.height
        pos = x.strong.y + height
        index = int(pos / height)
        self.__add_label(index)
