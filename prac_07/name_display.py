from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder


class DisplayNames(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob", "Jim", "Cam", "Sam"]

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Display Names"
        self.root = Builder.load_file('name_displays.kv')
        self.create_widgets()

        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name, id=name)
            self.root.ids.names_box.add_widget(temp_label)


DisplayNames().run()
