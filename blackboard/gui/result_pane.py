import gi
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk, Gio  # noqa


class result_pane(Gtk.Box):
    def __init__(self):
        Gtk.Box.__init__(self)
        self.orientation = Gtk.Orientation.VERTICAL
        self.spacing = 0
