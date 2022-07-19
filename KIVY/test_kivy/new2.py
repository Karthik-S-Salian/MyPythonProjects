from kivy.app import App
from kivy.config import Config
from math import cos,sin,pi

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.graphics import Ellipse
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.screenmanager import Screen


class Pong(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            self.ball = Ellipse(pos=(0, 50), size=(self.ball_size, self.ball_size))
        self.init_angle=pi/4
        self.init_speed=dp(5)
        self.init_x=0
        self.time=0


    def on_parent(self,m,n):
        #Clock.schedule_interval(self.update_ball, 1 / 59)
        pass

    def on_size(self, *args):  # internal function
        #self.ball.pos = self.center
        pass


    def update_ball(self,dt):
        self.time+=0.01
        self.init_x=self.init_x+self.init_speed*cos(self.init_angle)*self.time
        y=self.init_speed*sin(self.init_angle)*self.time - 5*self.time*self.time
        #y=self.height-y*5
        y=y*80
        if y<0:
            self.time=0

        print(y)
        self.ball.pos=(self.init_x,y)


def main():
    class Test(App):
        def build(self):
            return Pong()

    Test().run()

if __name__=="__main__":
    main()



