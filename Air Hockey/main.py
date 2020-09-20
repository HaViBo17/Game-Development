import pygame
import math

pygame.init()

screen_width = 800
screen_height = 600
title = "Air Hockey"
icon = pygame.image.load("board-game.png")
gameOver = False

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)
pygame.display.set_icon(icon)
background = pygame.image.load("background.jpg")

# game settings
ai_mode = True
white = (255, 255, 255)
sp_blue = (27, 247, 2)
start_position_2 = (200 - 32, 325 - 32)
start_position_1 = (600 - 32, 325 - 32)
start_position_b = (400 - 16, 325 - 16)
puck1 = "circle (1).png"
puck2 = "circle (2).png"
goal_length = 200
line_thickness = 5
max_ball_speed = -1
min_ball_speed = -1
ball_size = -1
player_size = -1
cresponse = 5
presponse = 5
cof = 0.8
score1 = 0
score2 = 0
font = pygame.font.Font('freesansbold.ttf', 50)
textX2 = 10
textY2 = 10
textX1 = 750
textY1 = 10
textXf = 230
textYf = 10


class Player:

    def __init__(self, position, front):
        self.x = position[0]
        self.y = position[1]
        self.v_x = 0
        self.v_y = 0
        self.face = pygame.image.load(front)

    def get_position(self):
        a = (self.x, self.y)
        return a

    def get_v_x(self):
        return self.v_x

    def get_v_y(self):
        return self.v_y

    def set_x(self, x_cor):
        self.x = x_cor

    def set_y(self, y_cor):
        self.y = y_cor

    def set_v_x(self, vx):
        self.v_x = vx

    def set_v_y(self, vy):
        self.v_y = vy

    def think_and_play(self, ball):
        pass


class Ball:
    face = pygame.image.load("palau.png")

    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.v_x = 0
        self.v_y = 0

    def get_position(self):
        a = (self.x, self.y)
        return a

    def get_v_x(self):
        return self.v_x

    def get_v_y(self):
        return self.v_y

    def set_x(self, x_cor):
        self.x = x_cor

    def set_y(self, y_cor):
        self.y = y_cor

    def set_v_x(self, vx):
        self.v_x = vx

    def set_v_y(self, vy):
        self.v_y = vy


def collision(position1, position2, position3):
    distance1 = math.sqrt(math.pow(position1[0] + 16 - position3[0], 2) + math.pow(position1[1] + 16 - position3[1], 2))
    distance2 = math.sqrt(math.pow(position2[0] + 16 - position3[0], 2) + math.pow(position2[1] + 16 - position3[1], 2))
    if distance1 < distance2:
        if distance1 < 50:
            return 1
    else:
        if distance2 < 50:
            return 2


def mod(arrow):
    a = math.sqrt(math.pow(arrow[0], 2) + math.pow(arrow[1], 2))
    if a == 0:
        return 1
    return a


def dot(arrow1, arrow2):
    return arrow1[0] * arrow2[0] + arrow1[1] * arrow2[1]


def printa(arrow):
    print(arrow[0], arrow[1])


running = True
chintu = Player(start_position_1, puck1)
pintu = Player(start_position_2, puck2)
laddu = Ball(start_position_b)
while running:
    screen.blit(background, (0, 0))
    pygame.draw.line(screen, white, (25, 75), (775, 75), line_thickness)
    pygame.draw.line(screen, white, (25, 575), (775, 575), line_thickness)
    pygame.draw.line(screen, white, (400, 75), (400, 575), line_thickness)
    pygame.draw.line(screen, white, (25, 75), (25, 575), line_thickness)
    pygame.draw.line(screen, white, (775, 75), (775, 575), line_thickness)
    pygame.draw.circle(screen, white, (400, 325), 100, line_thickness)
    pygame.draw.line(screen, sp_blue, (25, 325 - goal_length * 0.5), (25, 325 + goal_length * 0.5), line_thickness * 2)
    pygame.draw.line(screen, sp_blue, (775, 325 - goal_length * 0.5), (775, 325 + goal_length * 0.5),
                     line_thickness * 2)
    if ai_mode:
        pos = (
            laddu.get_position()[0] - pintu.get_position()[0] - 16,
            laddu.get_position()[1] - pintu.get_position()[1] - 16)
        unit_pos = (pos[0] / mod(pos), pos[1] / mod(pos))
        if pos[0] > 0 and laddu.get_position()[0] < 360:
            pintu.set_v_x(unit_pos[0] * presponse)
            pintu.set_v_y(unit_pos[1] * presponse)
        else:
            pintu.set_v_x(-presponse)
            pintu.set_v_y(unit_pos[1] * presponse)

    # keep chintu in box
    if chintu.get_position()[0] > 711:
        chintu.set_x(711)
    elif chintu.get_position()[0] < 400:
        chintu.set_x(400)
    if chintu.get_position()[1] < 75:
        chintu.set_y(75)
    elif chintu.get_position()[1] > 511:
        chintu.set_y(511)

    # keep pintu in box
    if pintu.get_position()[0] > 336:
        pintu.set_x(336)
    elif pintu.get_position()[0] < 25:
        pintu.set_x(25)
    if pintu.get_position()[1] < 75:
        pintu.set_y(75)
    elif pintu.get_position()[1] > 511:
        pintu.set_y(511)

    # keep laddu in box
    if laddu.get_position()[0] > 743:
        laddu.set_x(743)
        laddu.set_v_x(- laddu.get_v_x() * cof)
    elif laddu.get_position()[0] < 25:
        laddu.set_x(25)
        laddu.set_v_x(-laddu.get_v_x() * cof)
    if laddu.get_position()[1] > 543:
        laddu.set_y(543)
        laddu.set_v_y(- laddu.get_v_y() * cof)
    elif laddu.get_position()[1] < 75:
        laddu.set_y(75)
        laddu.set_v_y(-laddu.get_v_y() * cof)

    # check collision
    collided = collision(chintu.get_position(), pintu.get_position(), laddu.get_position())
    if collided:
        if collided == 1:
            relative_position_ball = (
                laddu.get_position()[0] - chintu.get_position()[0], laddu.get_position()[1] - chintu.get_position()[1])
            relative_velocity_ball = (laddu.get_v_x() - chintu.get_v_x(), laddu.get_v_y() - chintu.get_v_y())
            unit_position = (relative_position_ball[0] / mod(relative_position_ball),
                             relative_position_ball[1] / mod(relative_position_ball))
            temp = dot(unit_position, relative_velocity_ball)
            if temp > 0:
                temp = 0
            change_velocity = (-2 * temp * unit_position[0], -2 * temp * unit_position[1])
            new_rel_velocity = (
                relative_velocity_ball[0] + change_velocity[0], relative_velocity_ball[1] + change_velocity[1])
            laddu.set_v_x(new_rel_velocity[0] * cof + chintu.get_v_x())
            laddu.set_v_y(new_rel_velocity[1] * cof + chintu.get_v_y())
        elif collided == 2:
            relative_position_ball = (
                laddu.get_position()[0] - pintu.get_position()[0], laddu.get_position()[1] - pintu.get_position()[1])
            relative_velocity_ball = (laddu.get_v_x() - pintu.get_v_x(), laddu.get_v_y() - pintu.get_v_y())
            unit_position = (relative_position_ball[0] / mod(relative_position_ball),
                             relative_position_ball[1] / mod(relative_position_ball))
            printa(relative_velocity_ball)
            temp = dot(unit_position, relative_velocity_ball)
            if temp > 0:
                temp = 0
            change_velocity = (-2 * temp * unit_position[0], -2 * temp * unit_position[1])
            new_rel_velocity = (
                relative_velocity_ball[0] + change_velocity[0], relative_velocity_ball[1] + change_velocity[1])
            laddu.set_v_x(new_rel_velocity[0] * cof + pintu.get_v_x())
            laddu.set_v_y(new_rel_velocity[1] * cof + pintu.get_v_y())

    # check goals
    if laddu.get_position()[0] > 740 and (laddu.get_position()[1] > 325 - goal_length * 0.5) and (
            laddu.get_position()[1] < 325 + goal_length * 0.5):
        score2 += 1
        laddu.set_x(start_position_b[0])
        laddu.set_y(start_position_b[1])
        pintu.set_x(start_position_2[0])
        pintu.set_y(start_position_2[1])
        chintu.set_x(start_position_1[0])
        chintu.set_y(start_position_1[1])
        laddu.set_v_x(0)
        laddu.set_v_y(0)
        pintu.set_v_x(0)
        pintu.set_v_y(0)
        chintu.set_v_x(0)
        chintu.set_v_y(0)
    elif laddu.get_position()[0] < 30 and (laddu.get_position()[1] > 325 - goal_length * 0.5) and (
            laddu.get_position()[1] < 325 + goal_length * 0.5):
        score1 += 1
        laddu.set_x(start_position_b[0])
        laddu.set_y(start_position_b[1])
        pintu.set_x(start_position_2[0])
        pintu.set_y(start_position_2[1])
        chintu.set_x(start_position_1[0])
        chintu.set_y(start_position_1[1])
        laddu.set_v_x(0)
        laddu.set_v_y(0)
        pintu.set_v_x(0)
        pintu.set_v_y(0)
        chintu.set_v_x(0)
        chintu.set_v_y(0)

        # go through all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if a keystroke is pressed check which key is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                chintu.set_v_x(-cresponse)
            if event.key == pygame.K_RIGHT:
                chintu.set_v_x(cresponse)
            if event.key == pygame.K_UP:
                chintu.set_v_y(-cresponse)
            if event.key == pygame.K_DOWN:
                chintu.set_v_y(cresponse)
            if event.key == pygame.K_a:
                pintu.set_v_x(-presponse)
            if event.key == pygame.K_d:
                pintu.set_v_x(presponse)
            if event.key == pygame.K_w:
                pintu.set_v_y(-presponse)
            if event.key == pygame.K_s:
                pintu.set_v_y(presponse)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                chintu.set_v_x(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                chintu.set_v_y(0)
            if event.key == pygame.K_a or event.key == pygame.K_d:
                pintu.set_v_x(0)
            if event.key == pygame.K_w or event.key == pygame.K_s:
                pintu.set_v_y(0)

    # update positions
    chintu.set_x(chintu.get_position()[0] + chintu.get_v_x())
    chintu.set_y(chintu.get_position()[1] + chintu.get_v_y())
    pintu.set_x(pintu.get_position()[0] + pintu.get_v_x())
    pintu.set_y(pintu.get_position()[1] + pintu.get_v_y())
    laddu.set_x(laddu.get_position()[0] + laddu.get_v_x())
    laddu.set_y(laddu.get_position()[1] + laddu.get_v_y())

    screen.blit(chintu.face, chintu.get_position())
    screen.blit(pintu.face, pintu.get_position())
    screen.blit(laddu.face, laddu.get_position())

    # show scores
    score2a = font.render(str(score2), True, (255, 255, 255))
    screen.blit(score2a, (textX2, textY2))
    score1a = font.render(str(score1), True, (255, 255, 255))
    screen.blit(score1a, (textX1, textY1))
    flex = font.render("AIR HOCKEY", True, white)
    screen.blit(flex, (textXf, textYf))

    if score2 > 8 or score1 > 8:
        running = False
        gameOver = True

    if gameOver:
        if score1 > score2:
            for i in range(0, 2000):
                pygame.time.wait((1))
                done = font.render("WINS", True, (255, 255, 255))
                screen.blit(done, (400, 200))
                pygame.display.update()
        else:
            for i in range(0, 2000):
                pygame.time.wait((1))
                done = font.render("WINS", True, (255, 255, 255))
                if ai_mode :
                    done = font.render("BOT WINS",True,white)
                    screen.blit(done,(100,200))
                else:
                    screen.blit(done, (150, 200))
                pygame.display.update()

    pygame.display.update()
