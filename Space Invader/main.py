import pygame
import math
import random

# initialise the game
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Title and window
pygame.display.set_caption("Space Wars -offline")
icon = pygame.image.load("player.png")
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480

# score
score = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

# game over
over_font = pygame.font.Font('freesansbold.ttf',32)
def game_over_text():
    over_score2 = font.render("GAME OVER ", True, (255, 255, 255))
    screen.blit(over_score2, (200, 250))
def show_score(x,y):
    score2 = font.render(str(score) ,True,(255,255,255))
    screen.blit(score2,(x,y))

def player(x, y):
    screen.blit(playerImg, (x, y))


# enemy
enemyImg = []
enemyX = []
enemyY = []
enemyXchange =[]
enemyYchange = []
num_of_enemies = 6
for i in range(0,num_of_enemies):
    enemyImg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(0, 50))
    enemyXchange.append(1)
    enemyYchange.append(0)

# bullet
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletXchange = 0
bulletYchange = 2
bulletState = "ready"


def fire_bullet(x, y):
    global bulletState
    bulletState = "fire"
    screen.blit(bulletImg, (x + 20, y + 10))


# background
background = pygame.image.load("background-min.png")


def enemy(x, y ,i):
    screen.blit(enemyImg[i], (x, y))


def is_collision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX + 20 - bulletX , 2) + math.pow(bulletY - enemyY +20 , 2))
    if distance < 35:
        return True
    else:
        return False


# event loop
running = True
playerXchange = 0

while running:
    # Game Over


    # screen color
    screen.blit(background, (0, 0))
    for event in pygame.event.get():  # go through all events
        if event.type == pygame.QUIT:
            running = False

        # if a keystroke is pressed check which key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerXchange = -0.7
            if event.key == pygame.K_RIGHT:
                playerXchange = 0.7
            if event.key == pygame.K_SPACE:
                if bulletState == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerXchange = 0
    if playerX > 736:
        playerX = 736
        playerXchange = 0
    if playerX < 0:
        playerX = 0
        playerXchange = 0
    playerX += playerXchange
    for i in range(0,num_of_enemies):
        if enemyY[i] > 440:
            for j in range(0, num_of_enemies):
                enemyY[j] = 1000
            game_over_text()
            running = False
            break
        if enemyX[i] > 736:
            enemyX[i] = 736
            enemyXchange[i] = -1
            enemyY[i] += 30
        if enemyX[i] < 0:
            enemyX[i] = 0
            enemyXchange[i] = 1
            enemyY[i] += 30
            # collision detection
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletState = "ready"
            bulletY = 480
            score += 2000 - enemyY[i]*2
            enemyX[i] = 10 * random.randint(0, 70)
            enemyY[i] -= 10 * random.randint(5,10)

        enemyX[i] += enemyXchange[i]
        enemy(enemyX[i], enemyY[i] , i)
    # Bullet movement
    if bulletY <= 0:
        bulletState = "ready"
        bulletY = 480
    if bulletState == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletYchange


    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()
