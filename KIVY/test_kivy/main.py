from kivy import Config, platform
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')
from SpaceLoot import SpaceGame
from MagicTiles import MagicTiles
from Pong import Pong


def is_desktop():
    if platform in ('linux', 'win', 'macosx'):
        return True
    else:
        return False


class ScreenHandler(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenHandler, self).__init__(**kwargs)
        self.transition = NoTransition()
        self.add_widget(MainScreen())
        self.add_widget(Pong(is_desktop))
        self.add_widget(SpaceGame(is_desktop))
        self.add_widget(MagicTiles(is_desktop))


class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.Games = ['bounce_ball', 'space_loot', 'magic_tile']
        lay = BoxLayout(orientation='vertical')
        self.add_widget(lay)
        for i in range(len(self.Games)):
            lay.add_widget(Button(text=self.Games[i], on_press=self.switch_screen))

    def switch_screen(self, instance):
        name = instance.text
        self.parent.current = name
        if name == self.Games[0]:
            pass


class TestApp(App):
    def build(self):
        return ScreenHandler()


TestApp().run()
