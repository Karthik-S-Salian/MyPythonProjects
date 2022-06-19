import pygame
from pygame.locals import *
import time
import random

size = 40

class GAME_OVER(Exception):
    def __init__(self):
        print("GAME OVER")

class Apple:
    def __init__(self, parent_screen):
        self.apple_img = pygame.image.load("resource/images/apple.jpg")
        self.parent_screen = parent_screen
        self.appleX = size * random.randint(2, 24)
        self.appleY = size * random.randint(2, 14)

    def draw(self):
        self.parent_screen.blit(self.apple_img, (self.appleX, self.appleY))
        print(self.appleX,self.appleY)

    def move(self):
        self.appleX = size * random.randint(2, 24)
        self.appleY = size * random.randint(2, 14)


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = pygame.image.load("resource/images/block.jpg")
        self.x = [size] * length
        self.y = [size] * length
        self.speed=3
        self.direction = ""

    def add_body(self):
        self.length += 1
        self.x.append(1000)
        self.y.append(1000)

    def draw(self):
        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))

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

    def snake_move(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == "UP":
            self.y[0] -= self.speed
        elif self.direction == "DOWN":
            self.y[0] += self.speed
        elif self.direction == "RIGHT":
            self.x[0] += self.speed
        elif self.direction == "LEFT":
            self.x[0] -= self.speed


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = pygame.display.set_mode((1000, 600))
        self.game_status = "RUN"
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        self.init_background()
        self.ding_wav = pygame.mixer.Sound("resource/music/ding.mp3")
        self.crash_wav = pygame.mixer.Sound("resource/music/audio_dead.mp3")
        self.fps=70
        self.clock = pygame.time.Clock()

    def collision(self, x1, y1, x2, y2):
        if abs(x2 - x1) < size and abs(y2 - y1) < size:
            return True

    def display_score(self):
        score_font = pygame.font.SysFont('arial', 30)
        score = score_font.render("SCORE: " + str(self.snake.length - 2), True, (255, 255, 255))
        self.surface.blit(score, (800, 10))

    def snake_collision(self):
        if self.snake.x[0] < 0 or self.snake.y[0] < 0 or self.snake.x[0] > 1000 or self.snake.y[0] > 600:
            return True
        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                return True
        return False

    def music(self, s_type):
        pygame.mixer.Sound.play(s_type)

    def init_background(self):
        self.bg_img = pygame.image.load("resource/images/background.jpg")
        self.surface.blit(self.bg_img, (0, 0))
        pygame.mixer.music.load("resource/music/bg_music_1.mp3")
        pygame.mixer.music.play()

    def play(self):
        self.surface.blit(self.bg_img, (0, 0))
        self.snake.snake_move()
        self.apple.draw()
        self.snake.draw()
        self.display_score()
        pygame.display.flip()

        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.appleX, self.apple.appleY):
            self.music(self.ding_wav)
            self.snake.add_body()
            self.apple.move()

        if self.snake_collision():
            self.music(self.crash_wav)
            raise GAME_OVER

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
                            self.snake.move_up()
                        if event.key == K_DOWN:
                            self.snake.move_down()
                        if event.key == K_RIGHT:
                            self.snake.move_right()
                        if event.key == K_LEFT:
                            self.snake.move_left()
                    elif self.game_status == "OVER":
                        if event.key == K_RETURN:
                            self.restart()

            try:
                if self.game_status == "RUN":
                    self.play()
            except GAME_OVER:
                self.game_over()
                self.game_status = "OVER"
            self.fps_update()



if __name__ == "__main__":
    game = Game()
    game.run()
