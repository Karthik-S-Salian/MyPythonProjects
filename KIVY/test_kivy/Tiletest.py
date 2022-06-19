import random
from kivy import platform
from kivy.config import Config
from kivy.core.audio import SoundLoader
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Quad, Triangle
from kivy.properties import NumericProperty, Clock, StringProperty
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import Screen

Config.set('graphics', 'width', '900')
Config.set('graphics', 'height', '400')

from kivy.core.window import Window


class Menu(RelativeLayout):
    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        self.b1 = Button(size_hint=(.2, .15), pos_hint={"center_x": .5, "center_y": .3})
        self.b1.bind(on_press=self.button_press)
        self.b1.background_normal = ''
        self.b1.background_color = [1, .3, .4, 1]
        self.add_widget(self.b1)

    def button_press(self, e):
        self.parent.on_menu_button_press()

    def on_touch_down(self, touch):
        if self.opacity == 0:
            return False
        return super(Menu, self).on_touch_down(touch)


class Main(Screen):
    menu = Menu()
    perspective_point_x = NumericProperty(0)
    perspective_point_y = NumericProperty(0)
    menu_button_title = StringProperty("START")
    menu_title = StringProperty("G   A   L   A   X   Y")
    score_text = StringProperty("SCORE 0")
    NO_V_LINES = 8
    TILE_WIDTH_CENT = 0.4
    current_y_loop = 0
    TILE_HEIGHT_CENT = .4
    NO_TILES = 3
    tile = []
    TILE_PADDING_CENT = 0.02
    tile_padding = 0
    SPEED_Y_RATIO = 0.010
    SPEED_X_RATIO = 0.015
    tile_coordinate = []
    SHIP_WIDTH = 0.1
    SHIP_HEIGHT = 0.035
    SHIP_BASE_Y = 0.04
    ship_centroid = (0, 0)
    ship = None
    ship_xy = [(0, 0)] * 3
    is_game_over = False
    is_game_started = False
    sound_begin = None
    sound_over = None
    sound_galaxy = None
    bg_music = None
    sound_impact = None
    sound_restart = None

    def __init__(self, **kwargs):
        super(Main, self).__init__(**kwargs)
        self.add_widget(self.menu)
        self.init_audio()
        self.sound_galaxy.play()
        self.init_tiles()
        self.init_ship()
        self.start_index = -int(self.NO_V_LINES / 2) + 1
        self.pre_fill_tile_xy()
        self.generate_tile_xy()
        self.current_offset_y = 0
        self.speed = 0
        self.current_offset_x = 0
        self.speed_x = 10
        self.c_speed_x = 0
        Clock.schedule_interval(self.update, 1 / 59)

    def reset_game(self):
        self.score_text = "SCORE 0"
        self.current_offset_x = 0
        self.current_y_loop = 0
        self.current_offset_y = 0
        self.c_speed_x = 0
        self.tile_coordinate = []
        self.pre_fill_tile_xy()
        self.generate_tile_xy()
        self.is_game_over = False
        Clock.schedule_interval(self.update, 1 / 59)

    def init_audio(self):
        self.sound_begin = SoundLoader.load("resources/audio/begin.wav")
        self.sound_over = SoundLoader.load("resources/audio/gameover_voice.wav")
        self.sound_galaxy = SoundLoader.load("resources/audio/galaxy.wav")
        self.bg_music = SoundLoader.load("resources/audio/music1.wav")
        self.sound_impact = SoundLoader.load("resources/audio/gameover_impact.wav")
        self.sound_restart = SoundLoader.load("resources/audio/restart.wav")

        self.sound_begin.volume = 1
        self.sound_over.volume = .25
        self.sound_galaxy.volume = .25
        self.bg_music.volume = .25
        self.sound_impact.volume = .6
        self.sound_restart.volume = .25

    def keyboard_closed(self):
        self.keyboard.unbind(on_key_down=self.on_keyboard_down)
        self.keyboard.unbind(on_key_up=self.on_keyboard_up)
        self.keyboard = None

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        else:
            return False

    # automatically called when we attach current widget (MainWidget) to App class
    def on_parent(self, widget, parent):
        if self.is_desktop():
            self.keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self.keyboard.bind(on_key_down=self.on_keyboard_down)
            self.keyboard.bind(on_key_up=self.on_keyboard_up)


    # automatically called when display size changes
    def on_size(self, *args):
        self.perspective_point_x = self.width / 2
        self.perspective_point_y = self.height * 0.75
        self.update_ship()
        self.update(0)
        self.speed = self.height * self.SPEED_Y_RATIO
        self.speed_x = self.width * self.SPEED_X_RATIO
        self.tile_width_by_8 = self.TILE_WIDTH_CENT * self.width / 8
        self.tile_height_by_8 = self.TILE_HEIGHT_CENT * self.height / 8

    def init_ship(self):
        with self.canvas:
            Color(0, 0, 0)
            self.ship = Triangle()

    def update_ship(self):
        self.tile_padding = self.TILE_PADDING_CENT * self.height
        center_x = int(self.width / 2)
        base_y = int(self.SHIP_BASE_Y * self.height)
        top_y = int(base_y + self.SHIP_HEIGHT * self.height)
        ship_half_width = int(self.SHIP_WIDTH * self.width / 2)
        x1, y1 = self.transform(center_x - ship_half_width, base_y)
        x2, y2 = self.transform(center_x, top_y)
        x3, y3 = self.transform(center_x + ship_half_width, base_y)
        self.ship_centroid = (int((x1 + x2 + x3) / 3), int((y1 + y2 + y3) / 3))
        self.ship.points = [x1, y1, x2, y2, x3, y3]

    def check_ship_collision(self):
        for i in range(0, len(self.tile_coordinate)):
            ti_x, ti_y = self.tile_coordinate[i]
            if ti_y > self.current_y_loop + 1:
                return False
            if self.check_ship_tile_collide(ti_x, ti_y):
                return True
        return False

    def check_ship_tile_collide(self, ti_x, ti_y):
        x_min, y_min = self.get_tile_coordinate(ti_x, ti_y)
        x_max, y_max = self.get_tile_coordinate(ti_x + 1, ti_y + 1)
        px, py = self.ship_centroid
        if x_min - self.tile_width_by_8 <= px <= self.tile_width_by_8 + x_max:
            if y_min - self.tile_height_by_8 <= py <= y_max + self.tile_height_by_8:
                return True
        return False

    def get_line_x_from_index(self, index):
        spacing = self.TILE_WIDTH_CENT * self.width
        offset = index - 0.5
        line_x = int(self.perspective_point_x + offset * spacing + self.current_offset_x)
        return line_x

    def get_line_y_from_index(self, index):
        line_y = index * self.TILE_HEIGHT_CENT * self.height - self.current_offset_y
        return line_y

    def get_tile_coordinate(self, ti_x, ti_y):
        ti_y = ti_y - self.current_y_loop
        x = self.get_line_x_from_index(ti_x)
        y = self.get_line_y_from_index(ti_y)
        return x, y

    def pre_fill_tile_xy(self):
        for i in range(10):
            self.tile_coordinate.append((0, i))

    def init_tiles(self):
        with self.canvas:
            Color(1, 1, 1)
            for i in range(self.NO_TILES):
                self.tile.append(Quad())

    def generate_tile_xy(self):
        last_x = 0
        last_y = 0

        for i in range(len(self.tile_coordinate) - 1, -1, -1):
            if self.tile_coordinate[i][1] < self.current_y_loop:
                del self.tile_coordinate[i]

        loop = len(self.tile_coordinate)
        if loop > 0:
            last = self.tile_coordinate[-1]
            last_x = last[0]
            last_y = last[1] + 1

        for i in range(loop, self.NO_TILES):
            r = random.randint(0, 2)  # 0-> straight,1->right , 2->left
            if last_x - 1 <= self.start_index:
                r = 1
            if last_x + 1 >= (self.start_index + self.NO_V_LINES - 1):
                r = 2
            if r == 1:
                last_x += 1
                self.tile_coordinate.append((last_x, last_y))
                last_y += 1
                self.tile_coordinate.append((last_x, last_y))
            elif r == 2:
                last_x -= 1
                self.tile_coordinate.append((last_x, last_y))
                last_y += 1
                self.tile_coordinate.append((last_x, last_y))
            else:
                self.tile_coordinate.append((last_x, last_y))
            last_y += 1

    def update_tiles(self):
        for i in range(self.NO_TILES):
            ti_x, ti_y = self.tile_coordinate[i]
            x_min, y_min = self.get_tile_coordinate(ti_x, ti_y)
            x_max, y_max = self.get_tile_coordinate(ti_x + 1, ti_y + 1)
            x1, y1 = self.transform(x_min + self.tile_padding, y_min + self.tile_padding)
            x2, y2 = self.transform(x_min + self.tile_padding, y_max - self.tile_padding)
            x3, y3 = self.transform(x_max - self.tile_padding, y_max - self.tile_padding)
            x4, y4 = self.transform(x_max - self.tile_padding, y_min + self.tile_padding)
            self.tile[i].points = [x1, y1, x2, y2, x3, y3, x4, y4]

    def transform(self, x, y):
        # return self.transform_2D(x, y)
        return self.transform_perspective(x, y)

    def transform_2D(self, x, y):
        return int(x), int(y)

    def transform_perspective(self, x, y):
        linear_y = y * self.perspective_point_y / self.height
        if linear_y > self.perspective_point_y:
            linear_y = self.perspective_point_y
        diff_x = x - self.perspective_point_x
        diff_y = self.perspective_point_y - linear_y
        factor_y = diff_y / self.perspective_point_y
        factor_y = factor_y * factor_y
        tr_x = self.perspective_point_x + diff_x * factor_y
        tr_y = self.perspective_point_y - factor_y * self.perspective_point_y
        return int(tr_x), int(tr_y)

    def on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'left':
            self.c_speed_x = self.speed_x
        if keycode[1] == 'right':
            self.c_speed_x = -self.speed_x
        if self.is_game_over or not self.is_game_started:
            if keycode[1] == 'enter':
                self.on_menu_button_press()

        return True

    def on_keyboard_up(self, keyboard, keycode):
        self.c_speed_x = 0
        return True

    def on_touch_down(self, touch):
        if not self.is_game_over and self.is_game_started:
            if touch.x < self.width / 2:
                self.c_speed_x = self.speed_x
            else:
                self.c_speed_x = -self.speed_x
        return super(Main, self).on_touch_down(touch)

    def on_touch_up(self, touch):
        self.c_speed_x = 0

    def update(self, dt):
        self.update_tiles()
        if self.is_game_started and not self.is_game_over:
            time_factor = dt * 59
            self.current_offset_y += self.speed * time_factor
            spacing_y = self.TILE_HEIGHT_CENT * self.height
            while self.current_offset_y > spacing_y:
                self.current_offset_y -= spacing_y
                self.current_y_loop += 1
                self.score_text = "SCORE " + str(self.current_y_loop)
            self.generate_tile_xy()
            self.current_offset_x += self.c_speed_x * time_factor
            if not self.check_ship_collision() and not self.is_game_over:
                print("GAME OVER")
                self.menu_title = "G  A  M  E    O  V  E  R"
                self.menu_button_title = "RESTART"
                self.menu.opacity = 1
                self.is_game_over = True
                self.bg_music.stop()
                self.sound_impact.play()
                Clock.schedule_once(self.game_over_voice, 2)
                Clock.unschedule(self.update)

    def game_over_voice(self, dt):
        if self.is_game_over:
            self.sound_over.play()

    def on_menu_button_press(self):
        if self.is_game_started:
            self.reset_game()
            self.sound_restart.play()
        else:
            self.sound_begin.play()
        self.bg_music.play()
        self.is_game_started = True
        self.menu.opacity = 0


if __name__=="__main__":
    class TiletestApp(App):
        def build(self):
            return Main()


    TiletestApp().run()
