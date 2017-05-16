from .gui.mainwin import mainwin
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio # noqa


if __name__ == "__main__":
    mw = mainwin()
    mw.show_all()
    Gtk.main()
