import pygame
from random import randint

def collision(x1, y1, x2, y2, limitX=40, limitY=40):
    if abs(y2 - y1) < limitY and abs(x2 - x1) < limitX:
        raise GAME_OVER
    return False

img_size=40
head_size=40

class GAME_OVER(Exception):
    def __init__(self):
        print('GAME OVER')

class Apple:
    def __init__(self,surface,width,height):
        self.surface=surface
        self.width=width
        self.height=height
        self.apple_img=pygame.image.load("resource/images/apple.jpg")
        self.apple_x=randint(0,width/img_size)*img_size
        self.apple_y=randint(0,height/img_size)*img_size

    def spawn(self):
        self.apple_x = randint(0, self.width / img_size) * img_size
        self.apple_y = randint(0, self.height / img_size) * img_size

    def draw(self):
        self.surface.blit(self.apple_img,(self.apple_x,self.apple_y))

class Snake:
    def __init__(self,surface,width,height):
        self.surface=surface
        self.width=width
        self.height=height
        self.length=2
        self.current_direction='RIGHT'
        self.body=[((self.height//(2*img_size))*img_size-i*img_size,(self.height//(2*img_size))*img_size) for i in range(self.length)]


    def collision(self):
        x,y=self.body[0]
        if not ((0 < x < self.width) or (0 < y <600)):
            raise GAME_OVER
        for xi,yi in self.body[3:self.length]:
            if collision(x, y,xi, yi):
                raise GAME_OVER

    def move(self):
        xbefore,ybefore=x,y=self.body[0]
        for xi,yi in self.body[1:]:
            xi,xbefore = xbefore,xi
            yi,ybefore = ybefore,yi
        if self.current_direction == "UP":
            y -= img_size
        elif self.current_direction == "DOWN":
            y += img_size
        elif self.current_direction == "RIGHT":
            x += img_size
        elif self.current_direction == "LEFT":
            x -= img_size

    def move_right(self):
        if not self.direction == "LEFT":
            self.direction = "RIGHT"

    def move_left(self):
        if not self.direction == "RIGHT":
            self.direction = "LEFT"

    def move_up(self):
        if not self.direction == "DOWN":
            self.direction = "UP"

    def move_down(self):
        if not self.direction == "UP":
            self.direction = "DOWN"


class Game:
    def __init__(self,width,height):
        pygame.init()
        self.width=(width//img_size)*img_size
        self.height=(height//img_size)*img_size




