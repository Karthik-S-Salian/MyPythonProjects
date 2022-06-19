from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Line, Rectangle, Ellipse
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty, Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget


class WindowManager(ScreenManager):
    def __init__(self, **kwargs):
        super(WindowManager, self).__init__(**kwargs)
        self.transition = NoTransition()
        self.add_widget(Screen5())
        self.add_widget(Screen6())
        self.add_widget(Screen7())
        self.add_widget(Screen8())

    def move(self, i):
        scr = "Screen" + str(i)
        self.switch_to(scr)


class Screen5(Screen):
    def __init__(self, **kwargs):
        super(Screen5, self).__init__(**kwargs)
        self.name = "Screen5"
        tool = ToolBar(CanvasExample5(), self)
        self.add_widget(tool)


class Screen6(Screen):
    def __init__(self, **kwargs):
        super(Screen6, self).__init__(**kwargs)
        self.name = "Screen6"
        tool = ToolBar(Button(text="6"), self)
        self.add_widget(tool)


class Screen7(Screen):
    def __init__(self, **kwargs):
        super(Screen7, self).__init__(**kwargs)
        self.name = "Screen7"
        tool = ToolBar(Button(text="7"), self)

        self.add_widget(tool)


class Screen8(Screen):
    def __init__(self, **kwargs):
        super(Screen8, self).__init__(**kwargs)
        self.name = "Screen8"
        tool = ToolBar(Button(text="8"), self)
        self.add_widget(tool)


class WidgetsLayoutExample(GridLayout):
    my_text = StringProperty(str(0))
    text_input_str = StringProperty("   ")
    count = 0
    count_enabled = BooleanProperty(False)

    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
        self.my_text = str(self.count)

    def on_toogle_button_state(self, widget):
        if widget.state == "normal":
            widget.text = "OFF"
            self.count_enabled = False
        else:
            widget.text = "ON"
            self.count_enabled = True

    def on_text_input_validate(self, widget):
        self.text_input_str = widget.text


#   def on_switch_active(self, widget):
#      self.should_slide=widget.active

    def on_slider_value(self, widget):
       print(widget.value)


class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(100):
            b = Button(text=str(i + 1), size_hint=(None, None), size=(dp(100), dp(100)))

            self.add_widget(b)


class CanvasExample4(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 400), width=2)
            Color(0, 1, 0, 1)
            Line(circle=(100, 100, 50), width=2)
            Line(rectangle=(400, 400, 80, 60), width=3)
            self.rect = Rectangle(pos=(600, 20), size=(80, 60))

    def on_button_click(self):
        sx, sy = self.rect.size
        x, y = self.rect.pos
        w = self.width
        inc = dp(20)
        if x + sx + inc > w:
            inc = w - x - sx
        print(inc)
        x += inc
        self.rect.pos = (x, y)


class CanvasExample5(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ball_size = dp(50)
        with self.canvas:
            self.ball = Ellipse(pos=(100, 100), size=(self.ball_size, self.ball_size))
        Clock.schedule_interval(self.update, 1 / 60)
        self.x_change = dp(3)
        self.y_change = dp(3)

    def on_size(self, *args):  # internal function
        self.ball.pos = self.center

    def update(self, dt):  # user defined dt must bcs Clock.schedule_interval(self.update,.5) dt=delta time (time
        # between function call)
        x, y = self.ball.pos
        w, h = self.ball.size
        c_x = x + self.x_change + w
        c_y = y + self.y_change + h
        if c_x > self.width or self.x_change + x < 0:
            self.x_change *= -1
        if c_y > self.height or self.y_change + y < 0:
            self.y_change *= -1
        x += self.x_change
        y += self.y_change
        self.ball.pos = (x, y)


class ToolBar(BoxLayout):
    def __init__(self, t, obj, **kwargs):
        super(ToolBar, self).__init__(**kwargs)
        self.object = obj
        self.g = t
        self.orientation = "vertical"
        buttons = list()
        self.call = 0
        self.add_widget(Button(text="A", size_hint=(1, .1)))
        inner = GridLayout(cols=10, size_hint=(1, .1))
        self.add_widget(inner)
        for i in range(4):
            buttons.append(Button(text="Screen" + str(i + 5), on_press=self.test))  # lambda a: self.test("fff")
            inner.add_widget(buttons[i])
        self.add_widget(self.g)

    def test(self, event):
        self.object.parent.current = event.text




class TheLabApp(App):
    pass

TheLabApp().run()
