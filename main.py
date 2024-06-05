from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 1
        self.res = TextInput(multiline=False)
        self.add_widget(self.res)

        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.button1 = Button(text="HELLO", font_size=40)
        self.inside.button1.bind(on_press=self.pressed1)
        self.inside.add_widget(self.inside.button1)

        self.inside.button2 = Button(text="WORLD", font_size=40)
        self.inside.button2.bind(on_press=self.pressed2)
        self.inside.add_widget(self.inside.button2)

        self.add_widget(self.inside)

    def pressed1(self, instance):
        self.res.text = self.inside.button1.text

    def pressed2(self, instance):
        self.res.text = self.inside.button2.text

class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()