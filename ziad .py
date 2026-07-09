from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class Calculator(App):
    def build(self):
        self.expression = ""

        main = GridLayout(cols=1, padding=10, spacing=10)

        self.screen = TextInput(
            text="0",
            readonly=True,
            font_size=40,
            halign="right",
            multiline=False,
            background_color=(0.1,0.1,0.1,1),
            foreground_color=(1,1,1,1)
        )

        main.add_widget(self.screen)

        buttons = GridLayout(cols=4, spacing=5)

        keys = [
            "7","8","9","/",
            "4","5","6","*",
            "1","2","3","-",
            "C","0","=","+"
        ]

        for key in keys:
            btn = Button(
                text=key,
                font_size=32
            )
            btn.bind(on_press=self.press)
            buttons.add_widget(btn)

        main.add_widget(buttons)

        return main

    def press(self, instance):
        key = instance.text

        if key == "C":
            self.expression = ""
            self.screen.text = "0"
            return

        if key == "=":
            try:
                self.expression = str(eval(self.expression))
            except:
                self.expression = ""
                self.screen.text = "Error"
                return
        else:
            self.expression += key

        if self.expression == "":
            self.screen.text = "0"
        else:
            self.screen.text = self.expression

Calculator().run()