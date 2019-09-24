from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder

names = ["Bob", "Jim", "Cam", "Sam"]


class DisplayNames(App):

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)

    def build(self):
        """Build the Kivy GUI."""
        self.title = "Display Names"
        self.root = Builder.load_file('name_displays.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in names:
            temp_button = Label(text=name, id=name)
            # temp_button.bind(on_release=self.press_entry)
            # add the button to the "entries_box" layout widget
            self.root.ids.names_box.add_widget(temp_button)


DisplayNames().run()
