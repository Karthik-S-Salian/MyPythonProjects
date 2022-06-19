import pygame
import random

# INITIALISING THE PYGAME
pygame.init()
# CREATING THE SCREEN
screen = pygame.display.set_mode((1200, 600))

# CLOCK TO CONTROL ITERATION SPEED
clock = pygame.time.Clock()

# ICON
pygame.display.set_caption("SPACE LOOT")
icon = pygame.image.load('resource/images/ufo.png')
pygame.display.set_icon(icon)

# PLAYER
player_img = pygame.image.load('resource/images/spaceship.png')
playerX = 30
playerY = 390
playerY_change = 0

#MOTION DISPLAYING LINES
lineX = []
lineY = []
no_of_line = 30
m = 6

for i in range(no_of_line):
    lineX.append(m)
    lineY.append(random.randint(460, 480))
    m += random.randint(35, 45)

#CACTUS
cactus_img=pygame.image.load('resource/images/alien (1).png')
cactusX=[]
cactusY=[]
no_of_cactus=3
cd=0
spawn=30

for c in range(no_of_cactus):
    cactusX.append(1200 + cd)
    cactusY.append(390)
    cd -=400

visible = True

# SCORE
score = 0

font = pygame.font.Font('freesansbold.ttf', 32)
font_over = pygame.font.Font('freesansbold.ttf', 60)


def show_score(score):
    display_score = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(display_score, (10, 10))


def game_over():
    display_game_over = font_over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(display_game_over, (250, 250))


def draw(img, x, y):
    screen.blit(img, (x, y))


def is_collide(object1_X, object1_Y, object2_X, object2_Y,lim=30):
    distanceX=abs(object1_X-object2_X)
    distanceY=abs(object1_Y-object2_Y)
    if distanceX<lim and distanceY<lim:
        return True

jump = False
x = 70
running = True
while running:
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if jump == False:
                if event.key == pygame.K_UP:
                    playerY_change = -4
                    playerY_change += -0.5
                    jump = True

    if jump == True:
        playerY += playerY_change
        if playerY <= 250:
            playerY_change = 4
        if playerY >= 390:
            playerY_change = 0
            jump = False

    draw(player_img, playerX, playerY)

    pygame.draw.line(screen, (0, 0, 0), (0, 450), (1200, 450), 2)

    for i in range(no_of_line):
        lineX[i] -= 2
        pygame.draw.line(screen, (0, 0, 0), (lineX[i], lineY[i]), (lineX[i] + 2, lineY[i]))
        if lineX[i] < 0:
            lineX[i] = 1200
            lineY[i] = random.randint(460, 480)

    for c in range(no_of_cactus):
        cactusX[c]-=2
        draw(cactus_img,cactusX[c],cactusY[c])

        if cactusX[c]<0:
            cactusX[c]=random.randint(1200,1800)

            print(spawn)

    if visible == False:
        game_over()
    show_score(score)

    clock.tick(x)
    if x <=90:
        x += 0.08
    pygame.display.flip()
    pygame.display.update()
