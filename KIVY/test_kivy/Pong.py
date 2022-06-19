
from kivy.core.window import Window
from kivy.graphics import Ellipse, Rectangle
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.screenmanager import Screen


class Pong(Screen):
    PADDLE_SPACE=0.2
    PADDLE_WIDTH=.1
    PADDLE_HEIGHT=.4
    def __init__(self,need_keyboard, **kwargs):
        super().__init__(**kwargs)
        self.is_desktop=need_keyboard
        self.name = 'bounce_ball'
        self.ball_size = dp(50)
        with self.canvas:
            self.ball = Ellipse(pos=(100, 100), size=(self.ball_size, self.ball_size))
        Clock.schedule_once(self.update, 1 / 59)
        self.x_change = dp(3)
        self.y_change = dp(3)
        self.paddle()
        self.right_paddle_x=0
        self.left_paddle_x=0

    def on_parent(self,m,n):
        print("parent")
        Clock.schedule_interval(self.update, 1 / 59)
        if self.is_desktop:
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self.keyboard.bind(on_key_down=self.on_keyboard_down)
            self.keyboard.bind(on_key_up=self.on_keyboard_up)

    def keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard.unbind(on_key_up=self.on_keyboard_up)
        self.keyboard = None

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        #print("sleep")
        #if keycode[1] == 'left':
        #    self.ship_c_shift = -self.ship_shift
        #if keycode[1] == 'right':
        #    self.ship_c_shift = self.ship_shift
        return True

    def on_keyboard_up(self, keyboard, keycode):
        #self.ship_c_shift = 0
        return True

    def on_touch_down(self, touch):
        pass
        #if touch.x < self.width / 2:
        #    self.ship_c_shift = -self.ship_shift
        #else:
        #    self.ship_c_shift = self.ship_shift

    def on_touch_up(self, touch):
        #self.ship_c_shift = 0
        pass

    def on_size(self, *args):  # internal function
        self.ball.pos = self.center
        x=self.width*self.PADDLE_WIDTH
        self.left_paddle_x=x
        self.right_paddle_x=self.width-x

    def paddle(self):
        with self.canvas:
            self.right_paddle=Rectangle()
            self.left_paddle=Rectangle()

    def update_paddle(self):
        self.left_paddle.pos=(self.left_paddle_x,self.height/2)
        self.right_paddle.pos=(self.right_paddle_x,self.height/2)

    def update(self, dt):  # user defined dt must bcs Clock.schedule_interval(self.update,.5)
        print("update")
        x, y = self.ball.pos
        w, h = self.ball.size
        self.update_paddle()
        c_x = x + self.x_change + w
        c_y = y + self.y_change + h
        if c_x > self.width or self.x_change + x < 0:
            self.x_change *= -1
        if c_y > self.height or self.y_change + y < 0:
            self.y_change *= -1
        x += self.x_change
        y += self.y_change
        self.ball.pos = (x, y)