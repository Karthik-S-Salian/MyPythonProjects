import pygame
from random import randint

# INITIALISING THE PYGAME
pygame.init()
# CREATING THE SCREEN
screen = pygame.display.set_mode((800, 600))

clock = pygame.time.Clock()

# TITLE & ICON
pygame.display.set_caption("SPACE INVADER")
icon = pygame.image.load('resource/images/ufo.png')
pygame.display.set_icon(icon)

# PLAYER
player_img = pygame.image.load('resource/images/spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# ENEMY
enemy_img = pygame.image.load('resource/images/alien (1).png')
enemyX = []
enemyY = []
enemyX_change = []
num_of_enemies = 11

for i in range(num_of_enemies):
    enemyX.append(randint(100, 700))
    enemyY.append(randint(30, 150))
    enemyX_change.append(2)

# BULLET
bullet_img = pygame.image.load('resource/images/bullet (1).png')
bulletX = 0
bulletY = 480
bulletY_change = 0
bullet_state = "ready"
collision =False

#SCORE
score_value=0
font=pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10
over = 0


font_over = pygame.font.Font('freesansbold.ttf', 60)

def game_over():
    display_game_over = font_over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(display_game_over, (250, 250))

def show_score(x,y):
    score = font.render("SCORE "+str(score_value),True,(255,255,255))
    screen.blit(score, (x, y))

# ADDING IMAGE TO THE SCREEN
def draw(img, x, y):
    if over ==0:
        screen.blit(img, (x, y))


def is_collide(object1_X, object1_Y, object2_X, object2_Y,lim=30):
    distanceX=abs(object1_X-object2_X)
    distanceY=abs(object1_Y-object2_Y)
    if distanceX<lim and distanceY<lim:
        return True


# GAME LOOP
running = True
while running:

    screen.fill((0,0,50))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # check spaceship movement command
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -2
            if event.key == pygame.K_RIGHT:
                playerX_change = 2

            if event.key == pygame.K_F1:
                if bullet_state == "ready":
                    bulletY_change = -6
                    bullet_state = "fire"
                    bulletX = playerX+20
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # PLAYER
    if playerX >= 740:
        playerX = 740
    if playerX <= 0:
        playerX = 0
    playerX += playerX_change
    draw(player_img,playerX, playerY)

    # ENEMY
    for i in range(num_of_enemies):
        if enemyX[i] > 740:
            enemyX[i] = 738
            enemyX_change[i] = -2
            enemyY[i] += 35
        if enemyX[i] < 5:
            enemyX[i] = 8
            enemyX_change[i] = 2
            enemyY[i] += 35
        if enemyY[i]  >= playerY and enemyX[i] == playerX:
            over = 1
            num_of_enemies = 0
        enemyX[i] += enemyX_change[i]
        draw(enemy_img, enemyX[i], enemyY[i])

        # COLLISION
        if bullet_state == "fire":
            collision=is_collide(enemyX[i]+16, enemyY[i]+16, bulletX+12, bulletY+12)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = randint(0, 780)
            enemyY[i] = randint(30, 150)
            collision=False

    # BULLET
    if bullet_state == "fire":
        if bulletY < 10:
            bulletY = 480
            bullet_state = "ready"
        bulletY += bulletY_change
        if bullet_state == "fire":
            draw(bullet_img,bulletX,bulletY)

    show_score(textX,textY)
    if over:
        game_over()
    clock.tick(100)
    pygame.display.update()
