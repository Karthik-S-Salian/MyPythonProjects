import pygame
from random import randint
from os.path import exists

class GAME_OVER(Exception):
    def __init__(self):
        print("GAME OVER")


def collision(x1, y1, x2, y2, limitX=35, limitY=35):
    if abs(y2 - y1) < limitY and abs(x2 - x1) < limitX:
        return True
    return False


class SuperCoin:
    def __init__(self, screen):
        self.screen = screen
        self.s_coin = pygame.mixer.Sound("resource/music/ding.mp3")
        self.super_coin_img = pygame.image.load('resource/images/powercoin.png')
        self.super_coinX = 100
        self.super_coinY = -400

    def move(self, shipX, shipY, score):
        self.super_coinY += 3
        if self.super_coinY > 600:
            self.super_coinX = randint(10, 790)
            self.super_coinY = 0
        elif collision(shipX, shipY, self.super_coinX, self.super_coinY):
            self.super_coinX = randint(10, 790)
            self.super_coinY = 0
            score += 5
            pygame.mixer.Sound.play(self.s_coin)
        self.screen.blit(self.super_coin_img, (self.super_coinX, self.super_coinY))
        return score


class Coin:
    def __init__(self, screen, no_of_coins):
        self.s_coin = pygame.mixer.Sound("resource/music/ding.mp3")
        self.screen = screen
        self.no_of_coins = no_of_coins
        self.coin_img = pygame.image.load('resource/images/coin.png')
        self.coinX = []
        self.coinY = []
        for i in range(self.no_of_coins):
            self.coinX.append(randint(10, 790))
            self.coinY.append(-700 + (i * 50))

    def move(self, shipX, shipY, score):
        for i in range(self.no_of_coins):
            self.coinY[i] += 3

            if self.coinY[i] > 600:
                self.coinX[i] = randint(10, 790)
                self.coinY[i] = 0
            elif collision(shipX, shipY, self.coinX[i], self.coinY[i]):
                self.coinX[i] = randint(10, 790)
                self.coinY[i] = 0
                score += 1
                pygame.mixer.Sound.play(self.s_coin)
            self.screen.blit(self.coin_img, (self.coinX[i], self.coinY[i]))
        return score

class Stars:
    def __init__(self, screen, no_of_stars):
        self.screen = screen
        self.no_of_stars = no_of_stars
        self.starX = []
        self.starY = []
        d_factor=600/no_of_stars
        for i in range(self.no_of_stars):
            self.starX.append(randint(10, 790))
            self.starY.append(d_factor + (i * d_factor))

    def move(self):
        for i in range(self.no_of_stars):
            self.starY[i] += 2
            if self.starY[i] > 600:
                self.starY[i] = 0
                self.starX[i] = randint(10, 780)
            pygame.draw.circle(self.screen,(255,255,255),(self.starX[i],self.starY[i]),3)

class Enemy:
    def __init__(self, screen, no_of_enemies):
        self.screen = screen
        self.s_enemy = pygame.mixer.Sound("resource/music/audio_dead.mp3")
        self.no_of_enemies = no_of_enemies
        self.enemy_img = pygame.image.load('resource/images/alien (1).png')
        self.enemyX = []
        self.enemyY = []
        for i in range(self.no_of_enemies):
            self.enemyX.append(randint(10, 790))
            self.enemyY.append(-1200 + (i * 100))

    def move(self, shipX, shipY):
        for i in range(self.no_of_enemies):
            self.enemyY[i] += 3
            if self.enemyY[i] > 600:
                self.enemyY[i] = 0
                self.enemyX[i] = randint(10, 780)
            if collision(shipX, shipY, self.enemyX[i] + 16, self.enemyY[i] + 16):
                pygame.mixer.Sound.play(self.s_enemy)
                raise GAME_OVER
            self.screen.blit(self.enemy_img, (self.enemyX[i], self.enemyY[i]))


class Spaceship:
    def __init__(self, screen):
        self.sship_img = pygame.image.load('resource/images/spaceship.png')
        self.spaceX = 350
        self.spaceY = 250
        self.spaceX_change = 0
        self.screen = screen

    def direction(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.spaceX_change = -2
            if event.key == pygame.K_RIGHT:
                self.spaceX_change = 2
        if event.type == pygame.KEYUP:
            self.spaceX_change = 0

    def move(self):
        self.spaceX += self.spaceX_change
        if self.spaceX > 740:
            self.spaceX = 740
        elif self.spaceX < 0:
            self.spaceX = 0
        self.screen.blit(self.sship_img, (self.spaceX, self.spaceY))


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.surface = self.init_bg()
        self.clock = pygame.time.Clock()
        self.fps = 70
        self.score = 0
        self.init_objects()
        self.is_fullscreen = 0
        self.game_status = 1  # game_status  0 = OVER , 1 = RUN , 2 = PAUSE
        self.restart_XY = (350, 320)
        self.quit_colour = (255, 255, 255)
        self.images_fonts()
        self.high_score = self.load_highscore()

    def init_bg(self):
        # BACK GROUND MUSIC
        pygame.mixer.music.load("resource/music/bg_music_1.mp3")
        pygame.mixer.music.play()

        # ICON
        pygame.display.set_caption("SPACE LOOT")
        icon = pygame.image.load('resource/images/alien (1).png')
        pygame.display.set_icon(icon)

        # SCREEN
        surface = pygame.display.set_mode((800, 600))
        return surface

    def init_objects(self):
        self.ship = Spaceship(self.surface)
        self.enemy = Enemy(self.surface, 5)
        self.coin = Coin(self.surface, 10)
        self.super_coin = SuperCoin(self.surface)
        self.stars = Stars(self.surface, 15)

    def images_fonts(self):
        self.bg_img = pygame.image.load('resource/images/space_1.jpg')
        self.font1 = pygame.font.Font('resource/fonts/Mojangles.ttf', 32)
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        over = pygame.font.Font('freesansbold.ttf', 60)
        self.i_over = over.render("GAME OVER", True, (255, 255, 255))
        self.i_restart = self.font.render("RESTART", True, (0, 0, 0))
        self.i_pause = pygame.image.load('resource/icons/exo_icon_pause.png')
        self.full_scr_img = pygame.image.load('resource/icons/exo_ic_fullscreen_enter.png')

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
        shipX = self.ship.spaceX + 32
        shipY = self.ship.spaceY + 32
        self.surface.blit(self.bg_img, (0, 0))
        self.surface.blit(self.i_pause, (10, 50))
        self.ship.move()
        self.enemy.move(shipX, shipY)
        self.stars.move()
        self.score = self.coin.move(shipX, shipY, self.score)
        self.score = self.super_coin.move(shipX, shipY, self.score)
        self.show_score(self.score)

    def pause(self):
        self.draw()
        pygame.mixer.music.pause()
        resume_img = pygame.image.load('resource/icons/exo_icon_play.png')
        self.game_status = 2
        self.surface.blit(resume_img, (350, 250))
        pygame.display.flip()

    def show_score(self, score):
        display_score = self.font1.render("SCORE: " + str(score), True, (255, 255, 255))
        self.surface.blit(display_score, (10, 10))

    def game_over(self):
        self.rewrite_highscore()
        self.surface.blit(self.bg_img, (0, 0))
        self.surface.blit(self.i_over, (250, 250))
        pygame.draw.rect(self.surface, (255, 255, 255), pygame.Rect(self.restart_XY[0], self.restart_XY[1], 150, 30))
        self.surface.blit(self.i_restart, self.restart_XY)
        display_score = self.font.render("HIGH SCORE: " + str(self.high_score), True, (255, 255, 255))
        self.surface.blit(display_score, (290, 150))

    def option(self):
        if not self.is_fullscreen:
            self.surface.blit(self.full_scr_img, (10, 50))

    def fps_update(self):
        self.fps += 0.01
        self.clock.tick(self.fps)

    def restart(self):
        self.score = 0
        pygame.mixer.music.play()
        self.init_objects()
        self.fps = 70
        self.game_status = 1

    def init_fullscreen(self):
        self.is_fullscreen = 1
        self.surface = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
        if self.game_status == 2:
            self.draw()

    def fullscreen_mode(self):
        pygame.draw.rect(self.surface, self.quit_colour, pygame.Rect(760, 0, 40, 30))
        pygame.draw.line(self.surface, (0, 0, 0), (770, 25), (790, 5), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (770, 5), (790, 25), 2)

    def main_loop(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.game_status == 1:
                    self.ship.direction(event)

                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if collision(34, 74, mouseX, mouseY, 30, 30):
                            self.pause()

                elif self.game_status == 0:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if collision(self.restart_XY[0] + 75, self.restart_XY[1] + 15, mouseX, mouseY, 75, 15):
                            self.restart()
                        elif collision(28, 78, mouseX, mouseY, 18, 18):
                            self.init_fullscreen()
                else:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if collision(398, 298, mouseX, mouseY, 30, 30):
                            self.game_status = 1
                            pygame.mixer.music.unpause()
                        elif collision(28, 78, mouseX, mouseY, 18, 18):
                            self.init_fullscreen()
                if self.is_fullscreen:
                    mouseX, mouseY = pygame.mouse.get_pos()
                    if collision(mouseX, mouseY, 800, 0):
                        self.quit_colour = (255, 0, 0)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            running = False
                    else:
                        self.quit_colour = (255, 255, 255)
            try:
                if self.game_status == 1:
                    self.draw()
            except GAME_OVER:
                pygame.mixer.music.pause()
                self.game_status = 0

            if not self.game_status == 1:
                if self.game_status == 0:
                    self.game_over()
                self.option()
                self.show_score(self.score)
            if self.is_fullscreen:
                self.fullscreen_mode()
            pygame.display.flip()
            self.fps_update()


if __name__ == "__main__":
    game = Game()
    game.main_loop()
