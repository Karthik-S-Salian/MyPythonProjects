import math

from kivy.app import App
from kivy.graphics import Line, Color
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.slider import Slider
from kivy.uix.textinput import TextInput


class Fun_Graph(RelativeLayout):
    def __init__(self, **kwargs):
        super(Fun_Graph, self).__init__()
        self.xy_axis()
        self.x_division = 10
        self.y_division = 10
        self.numbers = list()
        self.field = list()

    def on_size(self, a, b):
        self.update_axis()
        self.draw_graph()

    def xy_axis(self):
        with self.canvas:
            self.x_axis = Line()
            self.y_axis = Line()
            Color(0,1,0)
            self.point=Line(width=2)

    def update_axis(self):
        self.x_axis.points = (0, self.height / 2, self.width, self.height / 2)
        self.y_axis.points = (self.width / 2, 0, self.width / 2, self.height)
        self.index_axis()

    def index_axis(self):
        first_x_point = self.width / self.x_division
        first_y_point = self.height / self.y_division

        a = self.x_division + self.y_division + 2 - len(self.numbers)
        if a > 0:
            for i in range(a):
                n = Label()
                self.add_widget(n)
                self.numbers.append(n)
                with self.canvas:
                    self.field.append(Line())

        for i in range(self.x_division + 1):
            j = i - self.x_division / 2
            x = self.width / 2 + first_x_point * j
            self.numbers[i].pos = (first_x_point * j, dp(10))
            self.numbers[i].text = str(int(j))
            self.field[i].points = (x, 0, x, self.height)
        for i in range(self.y_division):
            j = i - self.y_division / 2
            y = self.height / 2 + j * first_y_point
            self.numbers[self.x_division + 1 + i].pos = (dp(10), j * first_y_point)
            self.numbers[self.x_division + 1 + i].text = str(int(j))
            self.field[self.x_division + 1 + i].points = (0, y, self.width, y)

    def draw_graph(self):

        z = self.x_division / 2
        x = -z
        points = list()
        while x < z:
            y = math.sin(x)
            points.append(self.width / 2 + x * self.width / self.x_division)
            points.append(self.height / 2 + y * self.height / self.y_division)
            x = x + 0.04

        self.point.points = points
        del points


class Main(BoxLayout):
    def __init__(self, **kwargs):
        super(Main, self).__init__()
        self.orientation = "vertical"
        self.add_widget(Fun_Graph())
        tool_bar = GridLayout(cols=2, size_hint=(1, .2))
        delta_h = Slider(min=0, max=100)
        delta_h.bind(value=self.on_delta)
        self.Delta_display = Label(text="h = 0")
        fun_input_1 = TextInput(text="function 1", multiline=False, on_text_validate=self.process_input_1)
        fun_input_2 = TextInput(text="function 2", multiline=False, on_text_validate=self.process_input_2)
        tool_bar.add_widget(fun_input_1)
        tool_bar.add_widget(delta_h)
        tool_bar.add_widget(fun_input_2)
        tool_bar.add_widget(self.Delta_display)
        self.add_widget(tool_bar)

    def on_delta(self, widget, value):
        self.Delta_display.text = "h = " + str(int(value))

    def on_size(self, a, b):
        pass

    def process_input_1(self, widget):
        print(widget.text)

    def process_input_2(self, widget):
        print(widget.text)


class GRAPHApp(App):
    def build(self):
        return Main()


GRAPHApp().run()
