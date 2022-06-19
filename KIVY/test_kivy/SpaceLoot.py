from kivy.core.window import Window
from kivy.properties import Clock
from kivy.uix.image import Image
from kivy.uix.screenmanager import Screen


class SpaceGame(Screen):
    def __init__(self,need_keyboard, **kwargs):
        super(SpaceGame, self).__init__(**kwargs)
        self.is_desktop=need_keyboard
        self.name = 'space_loot'
        self.ship = Image(source='resources/images/spaceship.png')
        self.add_widget(self.ship)
        self.ship_shift = 0
        self.ship_i_shift = 0
        self.ship_c_shift = 0


    def on_parent(self, m, n):
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
        if keycode[1] == 'left':
            self.ship_c_shift = -self.ship_shift
        if keycode[1] == 'right':
            self.ship_c_shift = self.ship_shift
        return True

    def on_keyboard_up(self, keyboard, keycode):
        self.ship_c_shift = 0
        return True

    def on_touch_down(self, touch):
        if touch.x < self.width / 2:
            self.ship_c_shift = -self.ship_shift
        else:
            self.ship_c_shift = self.ship_shift

    def on_touch_up(self, touch):
        self.ship_c_shift = 0

    def update(self, dt):
        self.ship_i_shift += self.ship_c_shift
        if self.ship_i_shift>self.width/2 or self.ship_i_shift<-self.width/2:
            self.ship_i_shift -= self.ship_c_shift
        self.ship.pos = (int(self.ship_i_shift), 0)

    def on_size(self, i, m):
        self.ship_shift = self.width * 0.008
