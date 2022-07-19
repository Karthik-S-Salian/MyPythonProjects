from kivy.app import App
from kivy.config import Config
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '500')

from kivy.core.window import Window
from kivy.graphics import Ellipse, Rectangle, Color
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.screenmanager import Screen

from collections import namedtuple

paddle=namedtuple('paddle',['obj','x_right','x_left','y_top','y_bottom'])

class Pong(Screen):
    PADDLE_SPACE=0.05
    PADDLE_WIDTH=.02
    PADDLE_HEIGHT=.4
    SPEED=0.005

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'bounce_ball'
        self.ball_radius = dp(20)
        with self.canvas:
            self.ball = Ellipse(size=(self.ball_radius, self.ball_radius))
        Clock.schedule_once(self.update, 1 / 59)
        self.padding=0
        self.x_change = dp(3)
        self.y_change = dp(3)
        self.right_paddle = paddle(0, 0, 0, 0, 0)
        self.left_paddle = paddle(0, 0, 0, 0, 0)
        self.paddle()
        self.moving_right=True
        #self.borders()
        self.speed=5
        self.game_state=1





    def borders(self):
        with self.canvas:
            Color(1,.5,0)
            self.bottom_border=Rectangle()
            self.top_border=Rectangle()
            self.right_border=Rectangle()
            self.left_border=Rectangle()


    def update_borders(self):
        border_width = self.height * 0.05
        border_width_side=self.width*0.02
        self.top_border.pos = (0, self.height - border_width)
        self.top_border.size = (self.width, border_width)
        self.bottom_border.size = (self.width, border_width)
        self.left_border.pos = (0, 0)
        self.left_border.size = (border_width_side, self.height)
        self.right_border.pos = (self.width-border_width_side, 0)
        self.right_border.size = (border_width_side, self.height)

    def on_parent(self,m,n):
        Clock.schedule_interval(self.update, 1 / 59)

    def on_touch_down(self, touch):
        pass
        if touch.x > self.width / 2:
            if touch.y < self.height / 2:
                if self.right_paddle_y > 0:
                    self.right_dy = -self.speed
                    print('cca')
            else:
                if self.right_paddle_y2 < self.height:
                    print('ccascas')
                    self.right_dy = self.speed
        else:
            if touch.y < self.height / 2:
                if self.left_paddle_y > 0:
                    self.left_dy = -self.speed
            else:
                if self.left_paddle_y2 < self.height:
                    self.left_dy = self.speed

    def on_touch_up(self, touch):
        self.right_dy=0
        self.left_dy=0


    def on_size(self, *args):
        self.speed=self.SPEED*self.height
        self.ball.pos = self.center
        #self.update_borders()
        self.resize_paddle()
        self.padding=0.5*self.ball_radius

    def resize_paddle(self):
        x=self.width*self.PADDLE_WIDTH
        self.paddle_span = self.PADDLE_HEIGHT * self.height
        space=self.PADDLE_SPACE * self.width
        self.left_paddle_x,self.left_paddle_y=space,self.paddle_span
        self.right_paddle_x, self.right_paddle_y = self.width - space-x, self.paddle_span
        self.right_paddle.size = (x, self.paddle_span)
        self.left_paddle.size = (x, self.paddle_span)
        self.left_paddle.pos = (self.left_paddle_x,self.left_paddle_y)
        self.right_paddle.pos = (self.right_paddle_x, self.right_paddle_y)
        self.right_paddle_x2=self.width - space
        self.left_paddle_x2=space+x
        self.right_paddle_y2 = self.right_paddle_y+self.paddle_span
        self.left_paddle_y2 = self.left_paddle_y+self.paddle_span


    def paddle(self):
        with self.canvas:
            Color(1, 1, 1)
            self.right_paddle=Rectangle()
            self.left_paddle=Rectangle()
            self.right_paddle_y = 0
            self.left_paddle_y = 0
            self.left_paddle_x = 0
            self.right_paddle_x = 0
            self.left_dy=0
            self.right_dy=0
            self.paddle_span=0


    def update_paddle(self):
        self.left_paddle_y+=self.left_dy
        self.right_paddle_y+=self.right_dy
        self.right_paddle_y2 = self.right_paddle_y + self.paddle_span
        self.left_paddle_y2 = self.left_paddle_y + self.paddle_span
        self.left_paddle.pos=(self.left_paddle_x,self.left_paddle_y)
        self.right_paddle.pos=(self.right_paddle_x,self.right_paddle_y)

    def game_over(self):
        self.game_state=0


    def update_ball(self):
        x, y = self.ball.pos
        x += self.x_change
        y += self.y_change
        self.ball.pos = (x, y)
        self.update_paddle()
        c_x = x + self.x_change + self.ball_radius
        c_y = y + self.y_change + self.ball_radius
        if c_y > self.height or self.y_change + y < 0:
            self.y_change *= -1
        if self.moving_right:
            c_x = x + self.x_change + self.ball_radius
            if self.right_paddle_x < c_x < self.right_paddle_x2:
                if self.right_paddle_y-self.padding < c_y < self.right_paddle_y2+self.padding:
                    self.x_change *= -1
                    self.moving_right = False
                    return
        else:
            if self.left_paddle_x < self.x_change + x < self.left_paddle_x2:
                if self.left_paddle_y -self.padding< self.x_change+y < self.left_paddle_y2 + self.padding:
                    self.x_change *= -1
                    self.moving_right = True
                    return
        if c_x > self.width or self.x_change + x < 0:
            self.x_change*=-1

    def update(self, dt):  # user defined dt must bcs Clock.schedule_interval(self.update,.5)
        if self.game_state:
            self.update_ball()




class Test(App):
    def build(self):
        return Pong()

Test().run()

