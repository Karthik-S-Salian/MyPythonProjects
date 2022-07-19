from kivy.app import App
from kivy.config import Config

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')


from kivy.core.window import Window
from kivy.graphics import Ellipse, Rectangle, Color
from kivy.metrics import dp
from kivy.properties import Clock
from kivy.uix.screenmanager import Screen


class Pong(Screen):
    PADDLE_SPACE=0.05
    PADDLE_WIDTH=.05
    PADDLE_HEIGHT=.5
    SPEED=0.005
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
        self.right_paddle_y=0
        self.left_paddle_y=0
        self.right_dy=0
        self.left_dy=0
        #self.borders()
        self.speed=0


    def borders(self):
        with self.canvas:
            Color(1,.2,0)
            self.bottom_border=Rectangle(pos=(0,0))
            self.top_border=Rectangle()


    def update_borders(self):
        border_width =self.height * 0.05
        self.top_border.pos = (0, self.height - border_width)
        self.top_border.size=(self.width, border_width)
        self.bottom_border.size=(self.width,border_width)

    def on_parent(self,m,n):
        print('update')
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
        return True

    def on_touch_down(self, touch):
        pass
        if touch.x > self.width / 2:
            if touch.y <self.height/2:
                if self.right_paddle_y>0:
                    self.right_dy= -self.speed
            else:
                if self.right_paddle_y < self.height:
                    self.right_dy = self.speed
        else:
            if touch.y <self.height/2:
                if self.left_paddle_y>0:
                    self.left_dy = -self.speed
            else:
                if self.left_paddle_y < self.height:
                    self.left_dy = self.speed

    def on_touch_up(self, touch):
        self.left_dy=0
        self.right_dy=0
        pass

    def on_size(self, *args):  # internal function
        self.speed=self.SPEED*self.height
        self.ball.pos = self.center
        #self.update_borders()
        x=self.width*self.PADDLE_WIDTH
        y=self.PADDLE_HEIGHT*self.height

        self.left_paddle_x=self.PADDLE_SPACE*self.width
        self.right_paddle_x=self.width-self.left_paddle_x-x
        self.right_paddle.size=(x,y)
        self.left_paddle.size = (x, y)

    def paddle(self):
        with self.canvas:
            Color(.3, 1, 1)
            self.right_paddle=Rectangle()
            self.left_paddle=Rectangle()

    def update_paddle(self):
        self.left_paddle_y+=self.left_dy
        self.right_paddle_y+=self.right_dy
        self.left_paddle.pos=(self.left_paddle_x,self.left_paddle_y)
        self.right_paddle.pos=(self.right_paddle_x,self.right_paddle_y)

    def update(self, dt):  # user defined dt must bcs Clock.schedule_interval(self.update,.5)
        print(self.x_change)
        x, y = self.ball.pos
        w, h = self.ball.size
        self.update_paddle()
        c_x = x + self.x_change + w
        c_y = y + self.y_change + h
        if c_x > self.width or self.x_change + x < 0:
            self.x_change *= -1
        if c_y > self.height or self.y_change+y< 0:
            self.y_change *= -1
        x += self.x_change
        y += self.y_change
        self.ball.pos = (x, y)

class Test(App):
    def build(self):
        return Pong(True)

Test().run()