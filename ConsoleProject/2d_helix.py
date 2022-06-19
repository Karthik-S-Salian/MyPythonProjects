from math import sin, pi
import pygame

pygame.init()
screen = pygame.display.set_mode((1300, 600))
clock = pygame.time.Clock()


def y_filter(y):
    return 600 - y


class helix_positive:
    def __init__(self):
        self.wave = pygame.image.load('resources/coin.png')
        direction = -1  # -1 -> right  ::  +1 -> left
        period = 100
        wave_len = 50
        self.w = (2 * pi) / period
        self.k = (2 * pi) / wave_len
        self.phase = 0
        self.amplitude = 100
        self.helix_speed = 1

    def loop(self):
        time = 0
        while True:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            waveX = (self.helix_speed * time) % 1300
            waveY = y_filter(300 + self.amplitude * sin((self.k * waveX - self.w * time + self.phase)))
            screen.blit(self.wave, (waveX, waveY))
            time += 1
            pygame.draw.line(screen, (255, 255, 255), (0, 300), (1300, 300), 2)

            clock.tick(90)
            pygame.display.flip()

class two_helix:
    def __init__(self):
        self.w_direction = 'p'
        period = 100
        wave_len = 500
        self.w = (2 * pi) / period
        self.k = (2 * pi) / wave_len
        self.ph = 0
        self.A = 100
        self.p_wave = pygame.image.load('resources/coin.png')
        self.n_wave = pygame.image.load('resources/red_icon.png')

    def loop(self):
        waveX=0
        t=0
        while True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

            if self.w_direction == 'p':
                waveY = y_filter(300 + self.A * sin((self.k * waveX + self.w * t +self.ph)))
                waveX += 1
                screen.blit(self.p_wave, (waveX, waveY))
                if waveX == 1300:
                    self.w_direction = 'n'

            else:
                waveY = y_filter(300 + self.A * sin((self.k * waveX - self.w * t + self.ph+pi/2)))
                waveX -= 1
                screen.blit(self.n_wave, (waveX, waveY))
                if waveX == 0:
                    self.w_direction = 'p'

            t = t + 1

            clock.tick(150)
            pygame.display.flip()


def main():
    helix = two_helix()
    helix.loop()


if __name__ == "__main__":
    main()
