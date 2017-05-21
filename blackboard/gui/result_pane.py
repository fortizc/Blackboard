import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, Gdk  # noqa


class result_pane(Gtk.Grid):
    def __init__(self):
        Gtk.Grid.__init__(self)
        self.lb_list = []
        self.__add_label_at(0)

    def __add_label_at(self, index):
        lb = Gtk.Label()
        self.lb_list.insert(index, lb)
        if (len(self.lb_list) - 1) > index:
            self.insert_row(index)
        self.attach(lb, 0, index, 1, 1)
        lb.show()

    def __get_cursor_position(self, txt_op):
        x = txt_op.get_cursor_locations()
        height = x.strong.height
        pos = x.strong.y
        index = int(pos / height)
        return index

    def __get_pressed_key(self, value):
        key = Gdk.keyval_name(value.keyval)
        return key

    def add_label_at_cursor(self, txt_op, value):
        key = self.__get_pressed_key(value)
        if key != 'Return':
            return
        index = self.__get_cursor_position(txt_op)
        self.__add_label_at(index + 1)

    def update_label(self, index, result):
        try:
            self.lb_list[index].set_label(str(result))
            self.lb_list[index].show()
        except IndexError:
            print('Label list index out of range')