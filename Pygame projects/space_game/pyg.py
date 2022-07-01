import pygame
import random

# INITIALISING THE PYGAME
pygame.init()

screen = pygame.display.set_mode((800, 600))

# CLOCK TO CONTROL ITERATION SPEED
clock = pygame.time.Clock()



# ICON
pygame.display.set_caption("SPACE LOOT")
icon = pygame.image.load('resource/images/ufo.png')
pygame.display.set_icon(icon)

# PLAYER
player_img = pygame.image.load('resource/images/spaceship.png')
playerX = 350
playerY = 300
playerX_change = 0

# ENEMY
enemy_img = pygame.image.load('resource/images/alien (1).png')
enemyX = []
enemyY = []
num_of_enemies = 5

for i in range(num_of_enemies):
    enemyX.append(random.randint(20, 780))
    enemyY.append(random.randint(30 + 70 * i, 40 + 70 * i))

# COIN
coin_img = pygame.image.load('resource/images/coin.png')
coinX = []
coinY = []
num_of_coins = 10

for i in range(num_of_coins):
    coinX.append(random.randint(30, 780))
    coinY.append(random.randint(30 + 70 * i, 40 + 70 * i))

# SUPERCOIN
supercoin_img = pygame.image.load('resource/images/powercoin.png')
supercoinX = random.randint(100, 700)
supercoinY = 0
game_status = 1

# SCORE
create_file = open("resource/spacelootscore.txt", "w")
score_file = open("resource/spacelootscore.txt", "r")
high_score = score_file.readline()
if high_score == "":
    high_score = str(0)
score = 0
scoreX = 10
scoreY = 10
high_score = 0

# MOUSE
mouseX = 0
mouseY = 0
restartX = 350
restartY = 320

font = pygame.font.Font('freesansbold.ttf', 32)
font_over = pygame.font.Font('freesansbold.ttf', 60)
quit_colour = (255, 255, 255)


def show_score(score):
    display_score = font.render("SCORE: " + str(score), True, (255, 255, 255))
    screen.blit(display_score, (scoreX, scoreY))


def game_over():
    display_game_over = font_over.render("GAME OVER", True, (255, 255, 255))
    screen.blit(display_game_over, (250, 250))
    display_restart = font.render("RESTART", True, (0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(restartX, restartY, 150, 30))
    screen.blit(display_restart, (restartX, restartY))


# BLIT IMAGES IN THE SCREEN
def draw(img, x, y):
    if game_status:
        screen.blit(img, (x, y))


# CHECKS DISTANCE BETWEEN TWO OBJECTS
def is_collide(x1,y1,x2,y2,lim=30):
    distanceX=abs(x1-x2)
    distanceY=abs(y1-y2)
    if distanceX<lim and distanceY<lim:
        return True



# CEATE READ & WRITE SCORE FILE
def score_file_read(score,high_score):
    if score > int(high_score):
        score_file = open("resource/spacelootscore.txt", "w")
        score_file.write(str(score))
        high_score=score
        score_file.close()
    return high_score


x = 70
running = True

# MAIN GAME LOOP
while running:
    screen.fill((0,0,50))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
        if not game_status:
            mouseX, mouseY = pygame.mouse.get_pos()
            # RESTARTING THE GAME
            if is_collide(mouseX, mouseY, restartX + 75, restartY + 15):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    game_status = 1
                    num_of_coins = 10
                    num_of_enemies = 5
                    x = 70
                    score = 0
                    playerX = 350
                    playerY = 300
                    for i in range(num_of_enemies):
                        enemyX[i] = random.randint(20, 780)
                        enemyY[i] = random.randint(30 + 70 * i, 40 + 70 * i)

    # PLAYER COORDINATE HANDLING
    playerX = playerX + playerX_change
    player_centerX = playerX + 25
    player_centerY = playerY + 32
    if playerX < 10:
        playerX = 10
    if playerX > 740:
        playerX = 740
    draw(player_img, playerX, playerY)

    # ENEMY COORDINATE HANDLING
    for i in range(num_of_enemies):
        enemyY[i] += 3
        if is_collide(player_centerX, player_centerY, enemyX[i] + 16, enemyY[i] + 16,40):
            num_of_enemies = 0
            num_of_coins = 0
            game_status = 0
            high_score = score_file_read(score,high_score)
        if enemyY[i] >= 550:
            enemyX[i] = random.randint(20, 780)
            enemyY[i] = 0
        draw(enemy_img, enemyX[i], enemyY[i])

    # COIN COLLECTION
    for i in range(num_of_coins):
        coinY[i] += 3
        if is_collide(player_centerX, player_centerY, coinX[i], coinY[i]):
            coinX[i] = (random.randint(100, 700))
            coinY[i] = (random.randint(30, 40))
            score = score + 1
        if coinY[i] >= 550:
            coinX[i] = (random.randint(100, 700))
            coinY[i] = 0
        draw(coin_img, coinX[i], coinY[i])

    # SUPER COIN COLLISION
    if game_status:
        supercoinY += 3
        if is_collide(player_centerX, player_centerY, supercoinX, supercoinY):
            supercoinX = (random.randint(100, 700))
            supercoinY = (random.randint(30, 40))
            score = score + 5
        if supercoinY >= 550:
            supercoinX = (random.randint(100, 700))
            supercoinY = 0
        draw(supercoin_img, supercoinX, supercoinY)
    else:
        game_over()
        display_score = font.render("HIGH SCORE: " + str(high_score), True, (255, 255, 255))
        screen.blit(display_score, (500, scoreY))
    show_score(score)

    # DELAY IN FRAME RATE / SECOND
    clock.tick(x)
    x += 0.01

    pygame.display.update()
