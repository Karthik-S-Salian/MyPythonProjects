import pygame
from math import sqrt

def ellipse(center=(0, 0), major_axis=None, minor_axis=None):
    if major_axis is None:
        major_axis = minor_axis
    elif minor_axis is None:
        minor_axis = major_axis
    if major_axis is None:
        return None
    a = major_axis / 2
    b = minor_axis / 2
    c_y = center[1]
    c_x = center[0]
    x = c_x - a
    lim = c_x + a

    while True:
        w = (a - x + c_x) * (a + x - c_x)
        y = sqrt(w) * (b / a)
        pygame.draw.circle(screen, (255, 255, 255), (x, y + c_y), 2)
        pygame.draw.circle(screen, (255, 255, 255), (x, c_y - y), 2)
        if x == lim:
            break
        x = x + 1

if __name__ == '__main__':

    pygame.init()

    screen = pygame.display.set_mode((800, 600))

    ellipse((400, 300), 400,200)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.flip()

