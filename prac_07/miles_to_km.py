
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesToKmApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Miles to Km"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_button_up(self, value):
        value += 1
        self.root.ids.input_text.text = str(value)

    def handle_button_down(self, value):
        value -= 1
        self.root.ids.input_text.text = str(value)

    def handle_convert(self, value):
        value = value / 1.6
        self.root.ids.output_label.text = str(value)


MilesToKmApp().run()
