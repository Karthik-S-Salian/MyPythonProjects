import pygame
from random import randint
from os.path import exists

from pygame import mixer, display, K_SPACE, QUIT, MOUSEBUTTONDOWN
from pygame.event import get
from pygame.font import Font
from pygame.image import load
from pygame.mouse import get_pos
from pygame.time import Clock




class GAME_OVER(Exception):
    def __init__(self):
        print("GAME OVER")


def collision(x1, y1, x2, y2, limitX=35, limitY=35):
    if abs(y2 - y1) < limitY and abs(x2 - x1) < limitX:
        return True
    return False

class Cactus:
    def __init__(self, screen, no_of_enemies):
        self.screen = screen
        self.s_enemy = pygame.mixer.Sound("resource/music/audio_dead.mp3")
        self.no_of_enemies = no_of_enemies
        self.cactus_img = pygame.image.load('resource/images/alien (1).png')
        self.cactusX = []
        self.cactusY = 390
        for i in range(self.no_of_enemies):
            x=1200
            self.cactusX.append(x)
            x+=200

    def move(self, shipX, shipY):
        for i in range(self.no_of_enemies):
            self.cactusX[i] -= 3
            if self.cactusX[i] < 0:
                self.cactusX[i] =1200+randint(100,200)

            if collision(shipX, shipY, self.cactusX[i] + 16, self.cactusY+ 16):
                pygame.mixer.Sound.play(self.s_enemy)
                #raise GAME_OVER
            self.screen.blit(self.cactus_img, (self.cactusX[i], self.cactusY))


class Dino:
    def __init__(self, screen):
        self.dino_img = load('resource/images/spaceship.png')
        self.dinoX = 100
        self.dinoY = 390
        self.x=0
        self.screen = screen

    def jump(self,jump):
        if jump:
            self.dinoY=self.dinoY+self.x*self.x-5*self.x
            self.x=self.x+0.15
            if self.dinoY>390:
                self.dinoY = 390
                self.x=0
                jump=0
        return jump

    def move(self):
        self.screen.blit(self.dino_img, (self.dinoX, self.dinoY))

class Game:
    def __init__(self):
        pygame.init()
        mixer.init()
        self.surface = self.init_bg()
        self.clock = Clock()
        self.fps = 70
        self.score = 0
        self.init_objects()
        self.should_jump=0
        self.game_status = 1  # game_status  0 = OVER , 1 = RUN , 2 = PAUSE
        self.restart_XY = (350, 320)
        self.images_fonts()
        self.high_score = self.load_highscore()

    def init_bg(self):
        # BACK GROUND MUSIC
        mixer.music.load("resource/music/bg_music_1.mp3")
        mixer.music.play()

        # ICON
        pygame.display.set_caption("SPACE LOOT")
        icon = load('resource/images/alien (1).png')
        display.set_icon(icon)

        # SCREEN
        surface = display.set_mode((1200, 600))
        return surface

    def init_objects(self):
        self.dino = Dino(self.surface)
        self.cactus = Cactus(self.surface, 5)

    def images_fonts(self):
        self.bg_img = load('resource/images/space_1.jpg')
        self.font =Font('freesansbold.ttf', 32)
        over = Font('freesansbold.ttf', 60)
        self.i_over = over.render("GAME OVER", True, (255, 255, 255))
        self.i_restart = self.font.render("RESTART", True, (0, 0, 0))
        self.i_pause = load('resource/icons/exo_icon_pause.png')
        self.full_scr_img = load('resource/icons/exo_ic_fullscreen_enter.png')

    def load_highscore(self):
        fpath = "resource/spacelootscore.txt"
        if exists(fpath):
            with open(fpath, 'r') as f:
                highscore = f.read()
                if highscore:
                    return highscore
        else:
            f = open(fpath, 'x')
            f.close()
        return 0


    def rewrite_highscore(self):
        if self.score > int(self.high_score):
            score_file = open("resource/spacelootscore.txt", "w")
            score_file.write(str(self.score))
            score_file.close()
            self.high_score = self.score


    def draw(self):
        #self.surface.blit(self.bg_img, (0, 0))
        self.surface.blit(self.i_pause, (10, 50))
        self.cactus.move(self.dino.dinoX + 32, self.dino.dinoY + 32)
        self.dino.move()
        self.show_score(self.score)

    def pause(self):
        self.draw()
        pygame.mixer.music.pause()
        resume_img = pygame.image.load('resource/icons/exo_icon_play.png')
        self.game_status = 2
        self.surface.blit(resume_img, (350, 250))
        pygame.display.flip()

    def show_score(self, score):
        display_score = self.font.render("SCORE: " + str(score), True, (255, 255, 255))
        self.surface.blit(display_score, (10, 10))

    def game_over(self):
        self.rewrite_highscore()
        #self.surface.blit(self.bg_img, (0, 0))
        self.surface.blit(self.i_over, (250, 250))
        pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(self.restart_XY[0], self.restart_XY[1], 150, 30))
        self.surface.blit(self.i_restart, self.restart_XY)
        display_score = self.font.render("HIGH SCORE: " + str(self.high_score), True, (255, 255, 255))
        self.surface.blit(display_score, (290, 150))


    def fps_update(self):
        self.fps += 0.01
        self.clock.tick(self.fps)

    def restart(self):
        self.score = 0
        pygame.mixer.music.play()
        self.init_objects()
        self.fps = 70
        self.game_status = 1

    def main_loop(self):
        running = True
        while running:
            self.surface.fill((255, 255, 255))
            for event in get():
                if event.type == QUIT:
                    running = False

                (mouseX, mouseY) = get_pos()

                if self.game_status == 1:
                    if event.type == pygame.KEYDOWN:
                        if event.key ==K_SPACE:
                            self.should_jump=1

                    if event.type ==MOUSEBUTTONDOWN:
                        if collision(34, 74, mouseX, mouseY, 30, 30):
                            self.pause()

                else:
                    if event.type == MOUSEBUTTONDOWN:
                        if collision(self.restart_XY[0] + 75, self.restart_XY[1] + 15, mouseX, mouseY, 75, 15):
                            self.restart()

            if self.should_jump==1:
                self.should_jump=self.dino.jump(self.should_jump)
            try:
                if self.game_status == 1:
                    self.draw()
            except GAME_OVER:
                mixer.music.pause()
                self.game_status = 0


            if self.game_status == 0:
                self.game_over()
                self.show_score(self.score)
            pygame.display.flip()
            self.fps_update()


if __name__ == "__main__":
    game = Game()
    game.main_loop()

