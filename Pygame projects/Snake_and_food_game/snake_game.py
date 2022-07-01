from time import sleep
from random import randint
from pygame.constants import K_DOWN, K_RIGHT, K_LEFT, K_RETURN, K_UP, KEYDOWN, QUIT
from pygame.image import load
from pygame import init,mixer,display,event
from pygame.font import SysFont
size = 32

class GAME_OVER(Exception):
    def __init__(self):
        print("GAME OVER")

class Apple:
    def __init__(self, parent_screen):
        self.apple_img = load("resource/images/food.png").convert()
        self.parent_screen = parent_screen
        self.appleX = size * randint(2, 13)
        self.appleY = size * randint(3, 13)

    def draw(self):
        self.parent_screen.blit(self.apple_img, (self.appleX, self.appleY))

    def move(self):
        self.appleX = size * randint(1, 14)
        self.appleY = size * randint(3, 13)


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = load("resource/images/snake_body.png").convert()
        self.x = [96] * length
        self.y = [96] * length
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
            self.y[0] -= size
        if self.direction == "DOWN":
            self.y[0] += size
        if self.direction == "RIGHT":
            self.x[0] += size
        if self.direction == "LEFT":
            self.x[0] -= size


class Game:
    def __init__(self):
        init()
        mixer.init()
        self.surface = display.set_mode((608, 608))
        self.init_background()
        self.game_status = "RUN"
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        self.ding_wav = mixer.Sound("resource/music/ding.mp3")
        self.crash_wav = mixer.Sound("resource/music/audio_dead.mp3")

    def collision(self, x1, y1, x2, y2):
        if abs(x2 - x1) < size and abs(y2 - y1) < size:
            return True

    def display_score(self):
        score_font = SysFont('arial', 30)
        score = score_font.render(str(self.snake.length - 2), True, (255, 255, 255))
        self.surface.blit(score, (64, 20))

    def snake_collision(self):
        if self.snake.x[0] < 32 or self.snake.y[0] < 96 or self.snake.x[0] > 545 or self.snake.y[0] > 545:
            return True
        for i in range(3, self.snake.length):
            if self.collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                return True
        return False

    def init_background(self):
        self.bg_img = load("resource/images/ground.png")
        self.surface.blit(self.bg_img, (0, 0))
        mixer.music.load("resource/music/bg_music_1.mp3")
        mixer.music.play()

    def play(self):
        self.surface.blit(self.bg_img, (0, 0))
        self.snake.snake_move()

        if self.collision(self.snake.x[0], self.snake.y[0], self.apple.appleX, self.apple.appleY):
            mixer.Sound.play(self.ding_wav)
            self.snake.add_body()
            self.apple.move()

        if self.snake_collision():
            mixer.Sound.play(self.crash_wav)
            raise GAME_OVER

        self.snake.draw()
        self.apple.draw()
        self.display_score()
        display.update()

    def game_over(self):
        mixer.music.pause()
        over_font = SysFont('arial', 50)
        over = over_font.render("GAME OVER", True, (255, 255, 255))
        restart = over_font.render("TO RESTART PRESS ENTER", True, (255, 255, 255))
        self.surface.blit(over, (200, 200))
        self.surface.blit(restart, (25, 300))
        self.display_score()
        display.update()

    def restart(self):
        mixer.music.unpause()
        self.snake = Snake(self.surface, 2)
        self.apple = Apple(self.surface)
        self.game_status = "RUN"

    def run(self):
        running = True
        while running:
            for eve in event.get():
                if eve.type == QUIT:
                    running = False
                if eve.type == KEYDOWN:
                    if self.game_status == "RUN":
                        if eve.key == K_UP:
                            self.snake.move_up()
                        if eve.key == K_DOWN:
                            self.snake.move_down()
                        if eve.key == K_RIGHT:
                            self.snake.move_right()
                        if eve.key == K_LEFT:
                            self.snake.move_left()
                    elif self.game_status == "OVER":
                        if eve.key == K_RETURN:
                            self.restart()

            try:
                if self.game_status == "RUN":
                    self.play()
            except GAME_OVER:
                self.game_over()
                self.game_status = "OVER"
            sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
