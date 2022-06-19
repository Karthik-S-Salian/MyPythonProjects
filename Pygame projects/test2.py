import pygame
import random
from pygame import K_RETURN, K_LEFT, K_RIGHT, K_DOWN, K_UP, KEYDOWN, QUIT

size = 3

Direction=("UP",'DOWN','RIGHT','LEFT')

def collision(x1, y1, x2, y2, limitX=40, limitY=40):
    if abs(y2 - y1) < limitY and abs(x2 - x1) < limitX:
        raise GAME_OVER
    return False

class GAME_OVER(Exception):
    def __init__(self):
        print('GAME OVER')


class Apple:
    def __init__(self, parent_screen):
        self.apple_img = pygame.image.load("resource/images/apple.jpg")
        self.parent_screen = parent_screen
        self.appleX = size * random.randint(2, 24)
        self.appleY = size * random.randint(2, 14)

    def draw(self):
        self.parent_screen.blit(self.apple_img, (self.appleX, self.appleY))
        pygame.display.flip()

    def move(self):
        self.appleX = size * random.randint(2, 24)
        self.appleY = size * random.randint(2, 14)


class Snake:
    def __init__(self, parent_screen, length,width,height):
        self.length = length
        self.parent_screen = parent_screen
        self.width=width
        self.height=height
        self.block = pygame.image.load("resource/images/block.jpg")
        self.x=0
        self.y=0
        self.head=(self.x,self.y)
        self.body=[(self.head[0]+i*size,self.head[2]+i*size) for i in range(length)]
        self.direction = ""
        self.

    def add_body(self):
        self.length += 1
        self.x.append(1000)
        self.y.append(1000)

    def draw(self,direction):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))

    def move_right(self):
        if not self.direction == "LEFT":
            self.direction = "RIGHT"

    def move(self):
        if self.current_direction=='UP':


    def move_left(self):
        if not self.direction == "RIGHT":
            self.direction = "LEFT"

    def move_up(self):
        if not self.direction == "DOWN":
            self.direction = "UP"

    def move_down(self):
        if not self.direction == "UP":
            self.direction = "DOWN"

    def snake_move(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == "UP":
            self.y[0] -= size
        elif self.direction == "DOWN":
            self.y[0] += size
        elif self.direction == "RIGHT":
            self.x[0] += size
        elif self.direction == "LEFT":
            self.x[0] -= size

    def collision(self):
        x,y=self.body[0]
        if not ((0 < x < self.width) or (0 < y <600)):
            raise GAME_OVER
        for xi,yi in self.body[3:self.length]:
            if collision(x, y,xi, yi):
                raise GAME_OVER

class Game:
    def __init__(self,screen_width,screen_height):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((screen_width, screen_height))
        self.game_status = "RUN"
        self.snake = Snake(self.surface, 2,screen_width,screen_height)
        self.apple = Apple(self.surface)
        self.init_background()
        self.ding_wav = pygame.mixer.Sound("resource/music/ding.mp3")
        self.crash_wav = pygame.mixer.Sound("resource/music/audio_dead.mp3")
        self.fps=70
        self.direction="RIGHT"
        self.clock = pygame.time.Clock()

    def collision(self, x1, y1, x2, y2):
        if abs(x2 - x1) < size and abs(y2 - y1) < size:
            return True

    def display_score(self):
        score_font = pygame.font.SysFont('arial', 30)
        score = score_font.render("SCORE: " + str(self.snake.length - 2), True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def music(self, s_type):
        pygame.mixer.Sound.play(s_type)

    def init_background(self):
        self.bg_img = pygame.image.load("resource/images/background.jpg")
        self.surface.blit(self.bg_img, (0, 0))
        pygame.mixer.music.load("resource/music/bg_music_1.mp3")
        pygame.mixer.music.play()

    def play(self,direction):
        self.surface.blit(self.bg_img, (0, 0))
        self.snake.snake_move()
        self.apple.draw()
        self.snake.draw(direction)
        self.display_score()
        pygame.display.flip()

        if self.collision(*self.snake.body[0], self.apple.appleX, self.apple.appleY):
            self.music(self.ding_wav)
            self.snake.add_body()
            self.apple.move()

    def game_over(self):
        pygame.mixer.music.pause()
        self.display_score()
        self.surface.blit(self.bg_img, (0, 0))
        over_font = pygame.font.SysFont('arial', 50)
        over = over_font.render("GAME OVER", True, (255, 255, 255))
        restart = over_font.render("TO RESTART PRESS ENTER", True, (255, 255, 255))
        self.surface.blit(over, (400, 250))
        self.surface.blit(restart, (250, 350))
        pygame.display.flip()

    def restart(self):
        pygame.mixer.music.unpause()
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        self.game_status = "RUN"

    def fps_update(self):
        self.fps += 0.01
        self.clock.tick(self.fps)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                if event.type == KEYDOWN:
                    if self.game_status == "RUN":
                        if event.key == K_UP:
                            self.direction=Direction[0]
                        if event.key == K_DOWN:
                            self.direction=Direction[1]
                        if event.key == K_RIGHT:
                            self.direction=Direction[2]
                        if event.key == K_LEFT:
                            self.direction=Direction[3]
                    elif self.game_status == "OVER":
                        if event.key == K_RETURN:
                            self.restart()

            try:
                if self.game_status == "RUN":
                    self.play(self.direction)
            except GAME_OVER:
                self.music(self.crash_wav)
                self.game_over()
                self.game_status = "OVER"
            self.fps_update()


if __name__ == "__main__":
    game = Game(1000,600)
    game.run()