import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio  # noqa


class result_pane(Gtk.Grid):
    def __init__(self):
        super().__init__()
        self.lb_list = []
        self.add_label_at(0)

    def add_label_at(self, index):
        lb = Gtk.Label()
        self.lb_list.insert(index, lb)
        if (len(self.lb_list) - 1) > index:
            self.insert_row(index)
        self.attach(lb, 0, index, 1, 1)
        lb.set_label(str(index))
        lb.show()

    def update_label(self, index, result):
        try:
            self.lb_list[index].set_label(str(result))
            self.lb_list[index].show()
        except IndexError:
            print('Label list index out of range')
