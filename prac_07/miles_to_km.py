
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

CONST = 1.6


class MilesToKmApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (200, 100)
        self.title = "Miles to Km"
        self.root = Builder.load_file('miles_to_km.kv')
        return self.root

    def handle_button_up(self, value):
        valid_input = False
        while not valid_input:
            value = self.root.ids.input_text.text
            try:
                value = float(value)
                value += 1
                valid_input = True
            except ValueError:
                self.root.ids.input_text.text = "0"
                print("Invalid Input")
            except TypeError:
                self.root.ids.input_text.text = "0"
                print("Invalid Input")
        self.root.ids.input_text.text = str(value)

    def handle_button_down(self, value):
        valid_input = False
        while not valid_input:
            value = self.root.ids.input_text.text
            try:
                value = float(value)
                value -= 1
                valid_input = True
            except ValueError:
                self.root.ids.input_text.text = "0"
                print("Invalid Input")
            except TypeError:
                self.root.ids.input_text.text = "0"
                print("Invalid Input")
        self.root.ids.input_text.text = str(value)

    def handle_convert(self, value):

        # value = float(value)
        # value = value / 1.6
        # self.root.ids.output_label.text = str(value)

        valid_input = False
        while not valid_input:
            value = self.root.ids.input_text.text
            try:
                value = float(value)
                value = value / CONST
                valid_input = True
            except ValueError:
                self.root.ids.input_text.text = "0"
                print("Invalid Input")
            except TypeError:
                self.root.ids.input_text.text = "0"
                print("Invalid Input")
        self.root.ids.output_label.text = str(value)


MilesToKmApp().run()
