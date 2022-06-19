from kivy import platform
from kivy.app import App
from kivy.core.window import Window
from kivy.properties import Clock
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen


class SpaceGame(Screen):
    def __init__(self, **kwargs):
        super(SpaceGame, self).__init__(**kwargs)
        self.name = 'space_loot'
        self.ship = Button(text="A")#Image(source='images/spaceship.png')
        self.add_widget(self.ship)
        self.ship_shift=0
        self.keyboard2 = Window.request_keyboard(self.keyboard_closed, self)
        self.keyboard2.bind(on_key_down=self.on_keyboard_down)
        self.keyboard2.bind(on_key_up=self.on_keyboard_up)
        self.ship_i_shift=0
        self.ship_c_shift = 0
        Clock.schedule_interval(self.update, 1 / 59)

    def keyboard_closed(self):
        self.keyboard2.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard2.unbind(on_key_up=self.on_keyboard_up)
        self.keyboard2 = None

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        else:
            return False

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.ship_c_shift = -self.ship_shift
        if keycode[1] == 'right':
            self.ship_c_shift = self.ship_shift
        return True

    def on_keyboard_up(self, keyboard, keycode):
        self.ship_c_shift=0
        return True



    def on_touch_down(self, touch):
        if touch.x < self.width / 2:
            self.ship_c_shift = -self.ship_shift
        else:
            self.ship_c_shift = self.ship_shift

    def on_touch_up(self, touch):
        self.ship_c_shift =0

    def update(self, dt):
        self.ship_i_shift+=self.ship_c_shift
        self.ship.pos = (self.ship_i_shift, 0)

    def on_size(self, i, m):
        self.ship_shift = self.width * 0.01



class LaboratoryApp(App):
    def build(self):
        return SpaceGame()

if __name__=="__main__":
    LaboratoryApp().run()