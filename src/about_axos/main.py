import gi
gi.require_version("Gtk", "4.0")
gi.require_version("Adw", "1")
from gi.repository import Gtk, Adw

class AboutApp(Adw.Application):
    def __init__(self):
        super().__init__(application_id="com.axos-project.about")

    def do_activate(self):
        # Load the .ui file
        builder = Gtk.Builder.new_from_resource("/com/axos-project/about_axos/window.ui")

        # Get the about window
        about_window = builder.get_object("aboutWindow")
        about_window.set_application(self)
        
        about_window.set_default_size(500, 550)
        about_window.set_resizable(False)
        
        try:
            with open("/etc/axos-version", "r") as version_file:
                axos_version = version_file.read().strip()
                about_window.set_property("version", axos_version)
        except FileNotFoundError:
            print("Version file not found")
            about_window.set_property("version", "Version file not found")
        
        # Show the about window
        about_window.present()

app = AboutApp()
app.run()