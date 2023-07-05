# import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image


class FirstApp(GridLayout):
    def __init__(self, **Kwargs):
        super(FirstApp, self).__init__()

        self.size_hint = (0.7, 0.8)
        self.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.cols = 1

        self.add_widget(Image(source="sayHelloHalloween.png"))

        self.LabelText = Label(
            text="Whats your Name ?",
            font_size=21,
            color="#fe7e13"
        )
        self.add_widget(self.LabelText)

        self.Name = TextInput(
            multiline=False,
            font_size=21,
            padding_y=(20, 20),
            size_hint=(1, 0.5),
        )
        self.add_widget(self.Name)

        self.Submit = Button(
            text="Submit",
            font_size=21,
            bold=True,
            background_color="#fe7e13",
            background_normal="",
            size_hint=(1, 0.5)
        )
        self.Submit.bind(on_press=self.CallBack)
        self.add_widget(self.Submit)

        # return self.to_window

    def CallBack(self, instance):
        self.LabelText.text = "Hellow " + self.Name.text + " !"


class BuildApp(App):
    def build(self):
        self.icon = "icon.jpg"
        return FirstApp()


if __name__ == "__main__":
    BuildApp().run()
