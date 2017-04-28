import gi
from gi.repository import Gtk, Gio

gi.require_version('Gtk', '3.0')


class mainwin(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(600, 400)
        self.connect('destroy', Gtk.main_quit)

        self.__add_scrolled_win()
        self.__add_txt_view()
        self.__add_header_bar()

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

    def __add_txt_view(self):
        self.txt_view = Gtk.TextView()
        self.scroll.add(self.txt_view)

    def __add_scrolled_win(self):
        self.scroll = Gtk.ScrolledWindow()
        self.scroll.set_hexpand(True)
        self.scroll.set_vexpand(True)
        self.add(self.scroll)


win = mainwin()
win.show_all()
Gtk.main()
