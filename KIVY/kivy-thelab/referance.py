from kivy.app import App
from kivy.uix.screenmanager import Screen


class Main(Screen):
    pass

class TestApp(App):
    def build(self):
        return Main()

if __name__=="__main__":
    TestApp().run()
