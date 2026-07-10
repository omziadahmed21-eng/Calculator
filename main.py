from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class Calculator(App):
    def build(self):
        self.expression = ""

        layout = GridLayout(cols=1, padding=10, spacing=10)

        self.display = TextInput(
            text="",
            readonly=True,
            font_size=32,
            multiline=False
        )
        layout.add_widget(self.display)

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            ".", "0", "=", "+",
            "C"
        ]

        grid = GridLayout(cols=4, spacing=5)

        for item in buttons:
            btn = Button(text=item, font_size=24)
            btn.bind(on_press=self.on_button_press)
            grid.add_widget(btn)

        layout.add_widget(grid)

        return layout

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            self.expression = ""

        elif text == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = "Error"

        else:
            self.expression += text

        self.display.text = self.expression


Calculator().run()