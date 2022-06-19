import math

from kivy.app import App
from kivy.graphics import Line
from kivy.uix.screenmanager import Screen


class Main(Screen):
    def __init__(self,**kwargs):
        super(Main, self).__init__(**kwargs)
        self.create_mirror()
        self.create_rays()

    def on_size(self,m,n):
        print(self.height)


    def create_mirror(self):
        with self.canvas:
            self.mirror=Line(circle=(200, 600/2,500), width=2)

    def create_rays(self):

        self.rayX=0
        self.rayY=500
        x=math.floor(math.sqrt(self.rayY**2-1))
        print(x)


class TestApp(App):
    def build(self):
        return Main()

if __name__=="__main__":
    TestApp().run()