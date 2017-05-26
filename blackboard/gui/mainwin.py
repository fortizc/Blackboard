from .result_pane import result_pane
import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio, Gdk  # noqa


class mainwin(Gtk.Window):
    def __init__(self):
        super().__init__()
        self.set_default_size(600, 400)
        self.connect('destroy', Gtk.main_quit)

        self.__add_scrolled_win()
        self.__add_txt_view()
        self.__add_paned()
        self.__add_header_bar()
        self.txt_op.grab_focus()

    def __get_cursor_position(self):
        strong = self.txt_op.get_cursor_locations().strong
        return int(strong.y / strong.height)

    def add_label_at_cursor(self, txt_op, value):
        key = Gdk.keyval_name(value.keyval)
        if key != 'Return':
            return
        index = self.__get_cursor_position()
        self.result_pane.add_label_at(index + 1)

    def __create_header_btn(self, icon_name):
        icon = Gio.ThemedIcon(name=icon_name)
        image = Gtk.Image.new_from_gicon(icon, Gtk.IconSize.BUTTON)
        return Gtk.Button(None, image=image)

    def __add_header_bar(self):
        header = Gtk.HeaderBar()
        header.set_show_close_button(True)
        header.props.title = "Blackboard"
        self.set_titlebar(header)

        self.btn_set = self.__create_header_btn("applications-system-symbolic")
        self.btn_add = self.__create_header_btn("tab-new-symbolic")
        header.pack_end(self.btn_set)
        header.pack_start(self.btn_add)

    def __add_paned(self):
        paned = Gtk.HPaned()
        paned.add1(self.txt_op)
        paned.add2(self.result_pane)
        self.scroll.add(paned)
        w = self.get_size().width
        paned.set_position(w - w / 3)

    def __add_txt_view(self):
        self.txt_op = Gtk.TextView()
        self.result_pane = result_pane()
        self.txt_op.connect("key-press-event",
                            self.add_label_at_cursor)

        self.__txt_buff = self.txt_op.get_buffer()
        self.__txt_buff.connect("mark-set", self.__move_scroll)

    def __move_scroll(self, buff, location, mark):
        height = self.txt_op.get_cursor_locations().strong.height
        self.scroll.get_vadjustment().set_value(buff.props.cursor_position * height)

    def __add_scrolled_win(self):
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_hexpand(True)
        self.scroll.set_vexpand(True)
        self.add(self.scroll)
