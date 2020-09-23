import pygame
import random

pygame.init()
# colours
RED = (255, 0, 0)
YELLOW = (250, 238, 2)
GREEN = (11, 247, 7)
BLUE = (5, 129, 245)
PURPLE = (255, 0, 255)
ORANGE = (255, 145, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

colour_list = [RED, YELLOW, GREEN, BLUE, PURPLE, ORANGE]

margin = 10
screen_width = 600
screen_height = 720 + 2 * margin
title = "Tetris"

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)

gameOver = False
score = 0

textX = margin + 450
textY = margin

font = pygame.font.Font('freesansbold.ttf', 32)


def show_score(x, y):
    score2 = font.render(str(score), True, (255, 255, 255))
    screen.blit(score2, (x, y))


# display screen
class Block:
    def __init__(self, position):
        self.colour = BLACK
        self.x = position[0]
        self.y = position[1]
        self.freeze = False

    def set_colour(self, color):
        if not self.freeze:
            self.colour = color

    def get_position(self):
        a = (self.x, self.y)
        return a

    def get_colour(self):
        return self.colour

    def showcase(self):
        pygame.draw.rect(screen, self.get_colour(), (self.x, self.y, 40, 40), 0)

    def set_freeze(self):
        self.freeze = True

    def check_freeze(self):
        return self.freeze


my_display = []
for i in range(0, 10):
    a = []
    for j in range(0, 19):
        a.append(Block((margin + i * 40, margin + j * 40)))
        if j == 18:
            a[18].set_freeze()
    my_display.append(a)

# the 8 parts
parts = [[(-1, 1), (1, 1), (-1, -1), (1, -1)],
         [(-1, 1), (-1, -1), (1, -1), (2, -1)],
         [(1, 1), (1, -1), (-1, -1), (-2, -1)],
         [(-1, 1), (-1, -1), (1, -1), (1, -2)],
         [(1, 1), (-1, -1), (1, -1), (-1, -2)],
         [(-1, 1), (-1, -1), (1, -1), (-1, -2)],
         [(1, 1), (1, -1), (-1, -1), (1, -2)],
         [(-2, -1), (-1, -1), (1, -1), (2, -1)]]


class Object:
    def __init__(self, position):
        self.colour = colour_list[random.randint(0, 5)]
        self.design = parts[random.randint(0, 7)]
        self.x = position[0]
        self.y = position[1]

    def rotate(self):
        for i in range(0, 4):
            tempx = self.design[i][0]
            tempy = self.design[i][1]
            a = (tempy, -tempx)
            self.design[i] = a

    def get_colour(self):
        return self.colour

    def get_design(self):
        return self.design

    def get_position(self):
        a = (self.x, self.y)
        return a


def update_display(inspection_object):
    key = True
    for i in range(0, 4):
        check_x = 100
        check_y = 100
        if inspection_object.get_design()[i][0] > 0:
            check_x = inspection_object.get_design()[i][0] + inspection_object.get_position()[0] - 1
        else:
            check_x = inspection_object.get_design()[i][0] + inspection_object.get_position()[0]

        if inspection_object.get_design()[i][1] > 0:
            check_y = inspection_object.get_position()[1] - inspection_object.get_design()[i][1]
        else:
            check_y = inspection_object.get_position()[1] - inspection_object.get_design()[i][1] - 1
        if (check_y >= 0 and check_y <= 18 and check_x >= 0 and check_x <= 9):
            if my_display[check_x][check_y].check_freeze():
                key = False
                return False
        if not (check_x >= 0 and check_x <= 9):
            key = False
            return False

    if key:
        for i in range(0, 4):
            check_x = 100
            check_y = 100
            if inspection_object.get_design()[i][0] > 0:
                check_x = inspection_object.get_design()[i][0] + inspection_object.get_position()[0] - 1
            else:
                check_x = inspection_object.get_design()[i][0] + inspection_object.get_position()[0]

            if inspection_object.get_design()[i][1] > 0:
                check_y = inspection_object.get_position()[1] - inspection_object.get_design()[i][1]
            else:
                check_y = inspection_object.get_position()[1] - inspection_object.get_design()[i][1] - 1
            if check_y >= 0 and check_y <= 18 and check_x >= 0 and check_x <= 9:
                my_display[check_x][check_y].set_colour(inspection_object.get_colour())

    return True


def freeze_object(inspection_object):
    for i in range(0, 4):
        check_x = 100
        check_y = 100
        if inspection_object.get_design()[i][0] > 0:
            check_x = inspection_object.get_design()[i][0] + inspection_object.get_position()[0] - 1
        else:
            check_x = inspection_object.get_design()[i][0] + inspection_object.get_position()[0]

        if inspection_object.get_design()[i][1] > 0:
            check_y = inspection_object.get_position()[1] - inspection_object.get_design()[i][1]
        else:
            check_y = inspection_object.get_position()[1] - inspection_object.get_design()[i][1] - 1
        if check_y >= 0 and check_y <= 18 and check_x >= 0 and check_x <= 9:
            my_display[check_x][check_y].set_freeze()
    global moving_part
    moving_part = False


def check_line():
    for j in range(0, 18):
        tool = True
        for i in range(0, 10):
            if not my_display[i][17 - j].check_freeze():
                tool = False
        if tool:
            global score
            score += 20 - j
            for i in range(0, 10):
                for k in range(1, 18 - j):
                    my_display[i][18 - j - k].colour = my_display[i][17 - j - k].colour
                    my_display[i][18 - j - k].freeze = my_display[i][17 - j - k].freeze
                my_display[i][0].colour = BLACK
                my_display[i][0].freeze = False


def check_over():
    tool = False
    for i in range(1, 9):
        if my_display[i][0].check_freeze():
            tool = True
    return tool




time = 0
move_left = False
move_right = False
move_rotate = False
pappu = True
while pappu:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pappu = False
moving_part = False
running = True
moving_object = Object((-100, -100))
test_object = Object((5, -2))
while running:
    screen.fill(BLACK)
    time += 1
    if not moving_part:
        drop_x = random.randint(2, 9)
        drop_y = -2
        moving_object = Object((drop_x, drop_y))
        moving_part = True
    if time % 50 == 0:
        moving_object.y += 1

    tool = update_display(moving_object)

    for box2 in my_display:
        for box in box2:
            if not box.check_freeze():
                box.set_colour(BLACK)
    pool = update_display(moving_object)
    if not pool:
        moving_object.y -= 1
        update_display(moving_object)
        freeze_object(moving_object)

    for box2 in my_display:
        for box in box2:
            box.showcase()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left = True
                if event.key == pygame.K_RIGHT:
                    move_right = True
                if event.key == pygame.K_UP:
                    move_rotate = True
    if move_left:
        temp_object = Object(moving_object.get_position())
        temp_object.colour = BLACK
        temp_object.x -= 1
        if update_display(temp_object):
            moving_object.x -= 1
        move_left = False

    if move_right:
        temp_object = Object(moving_object.get_position())
        temp_object.colour = BLACK
        temp_object.x += 1
        if update_display(temp_object):
            moving_object.x += 1
        move_right = False

    if move_rotate:
        temp_object = Object(moving_object.get_position())
        temp_object.colour = BLACK
        temp_object.rotate()
        if update_display(temp_object) and temp_object.get_position()[0] <= 8 and temp_object.get_position()[0] >= 2:
            moving_object.rotate()
        move_rotate = False
    check_line()
    if check_over():
        gameOver = True

    if gameOver:
        print("GM")
        while True:
            pass
    pygame.draw.line(screen, WHITE, (margin, margin), (margin + 400, margin), 2)
    pygame.draw.line(screen, WHITE, (margin, margin), (margin, margin + 18 * 40), 2)
    pygame.draw.line(screen, WHITE, (margin + 400, margin), (margin + 400, margin + 18 * 40), 2)
    pygame.draw.line(screen, WHITE, (margin, margin + 18 * 40), (margin + 400, margin + 18 * 40), 2)
    for i in range(1, 18):
        pygame.draw.line(screen, BLACK, (margin, margin + i * 40), (margin + 400, margin + i * 40), 2)
    for i in range(1, 10):
        pygame.draw.line(screen, BLACK, (margin + i * 40, margin), (margin + i * 40, margin + 18 * 40), 2)
    show_score(textX, textY)
    score2 = font.render("T", True, colour_list[0])
    screen.blit(score2, (500, 100))
    score2 = font.render("E", True, colour_list[1])
    screen.blit(score2, (500, 150))
    score2 = font.render("T", True, colour_list[2])
    screen.blit(score2, (500, 200))
    score2 = font.render("R", True, colour_list[3])
    screen.blit(score2, (500, 250))
    score2 = font.render("I", True, colour_list[4])
    screen.blit(score2, (500, 300))
    score2 = font.render("S", True, colour_list[5])
    screen.blit(score2, (500, 350))
    pygame.display.update()
