from kivy.app import App
from kivy.uix.label import Label

class TheLabApp(App):

    def build(self):
        return Label(text="HELLO WORLD")


if __name__=="__main__":
    TheLabApp().run()