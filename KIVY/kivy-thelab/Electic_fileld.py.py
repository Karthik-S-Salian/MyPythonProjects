import math

from kivy.app import App
from kivy.graphics import Ellipse
from kivy.uix.relativelayout import RelativeLayout

E=1.6/10**19

class Charges:
    chargeMagnitude = E
    p_charge = {"charge_type": 1, "magnitude": chargeMagnitude, "pos": (100, 100), "object": None}
    n_charge = {"charge_type": -1, "magnitude": chargeMagnitude, "pos": (200, 200), "object": None}

    def update(self):
        l=math.pow(self.p_charge["pos"][0]-self.n_charge["pos"][0],2)+math.pow(self.p_charge["pos"][1]-self.n_charge["pos"][1],2)
        self.dipole_length=math.sqrt(l)
        print(self.dipole_length)



class Main(RelativeLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.charge=Charges()

    def on_size(self,m,n):
        self.update()
        self.charge.update()
        self.draw_charges()

    def draw_charges(self):
        with self.canvas:
            self.charge.p_charge["object"]=Ellipse(pos=self.charge.p_charge["pos"],size=(20,20))
            self.charge.n_charge["object"] = Ellipse(pos=self.charge.n_charge["pos"], size=(20, 20))

    def update(self):
        pass

class ElectricDipoleFieldApp(App):
    def build(self):
        return Main()


if __name__ == '__main__':
    ElectricDipoleFieldApp().run()


