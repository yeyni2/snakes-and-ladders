import pygame
import random
pygame.init()
WIDTH, HIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH + 200, HIGHT))
pygame.display.set_caption("snakes and ladders")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
LIGHT_BLUE = (176, 224, 230)
PURPLE = (128, 0, 128)
FPS = 20
BACKGROUND_IMAGE = pygame.image.load(r'..\snakes_and_ladders_board.jpg')
DICE_1_IMAGE = pygame.image.load(r'C:\Users\liran\Downloads\dice_1.jpeg')
DICE_2_IMAGE = pygame.image.load(r'C:\Users\liran\Downloads\dice_2.jpeg')
DICE_3_IMAGE = pygame.image.load(r'C:\Users\liran\Downloads\dice_3.jpeg')
DICE_4_IMAGE = pygame.image.load(r'C:\Users\liran\Downloads\dice_4.jpeg')
DICE_5_IMAGE = pygame.image.load(r'C:\Users\liran\Downloads\dice_5.jpeg')
DICE_6_IMAGE = pygame.image.load(r'C:\Users\liran\Downloads\dice_6.jpeg')
BACKGROUND = pygame.transform.scale(BACKGROUND_IMAGE, (1000, 1000))
DICE_1 = pygame.transform.scale(DICE_1_IMAGE, (100, 100))
DICE_2 = pygame.transform.scale(DICE_2_IMAGE, (100, 100))
DICE_3 = pygame.transform.scale(DICE_3_IMAGE, (100, 100))
DICE_4 = pygame.transform.scale(DICE_4_IMAGE, (100, 100))
DICE_5 = pygame.transform.scale(DICE_5_IMAGE, (100, 100))
DICE_6 = pygame.transform.scale(DICE_6_IMAGE, (100, 100))
screen.fill(PURPLE)
screen.blit(BACKGROUND, (0, 0))
pygame.display.update()
player1_color = RED
player2_color = YELLOW
player3_color = GREEN
player4_color = LIGHT_BLUE
snakes = {17: 7, 54: 34, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 79}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 71: 91, 80: 100}
BOARD = [[100, 99, 98, 97, 96, 95, 94, 93, 92, 91],
         [81, 82, 83, 84, 85, 86, 87, 88, 89, 90],
         [80, 79, 78, 77, 76, 75, 74, 73, 72, 71],
         [61, 62, 63, 64, 65, 66, 67, 68, 69, 70],
         [60, 59, 58, 57, 56, 55, 54, 53, 52, 51],
         [41, 42, 43, 44, 45, 46, 47, 48, 49, 50],
         [40, 39, 38, 37, 36, 35, 34, 33, 32, 31],
         [21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
         [20, 19, 18, 17, 16, 15, 14, 13, 12, 11],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]


def identify_location(locatoin):
    for i in range(10):
        for j in range(10):
            if BOARD[i][j] == locatoin:
                return True
    return False

def identify_location2(locatoin):
    for i in range(10):
        for j in range(10):
            if BOARD[i][j] == locatoin:
                return i, j

def draw_player1(player):
    pygame.draw.circle(screen, player1_color, (player[0], player[1]), 20)
    pygame.draw.circle(screen, BLACK, (player[0], player[1]), 20, 3)

def draw_player2(player):
    pygame.draw.circle(screen, player2_color, (player[0], player[1]), 20)
    pygame.draw.circle(screen, BLACK, (player[0], player[1]), 20, 3)

def draw_player3(player):
    pygame.draw.circle(screen, player3_color, (player[0], player[1]), 20)
    pygame.draw.circle(screen, BLACK, (player[0], player[1]), 20, 3)

def draw_player4(player):
    pygame.draw.circle(screen, player4_color, (player[0], player[1]), 20)
    pygame.draw.circle(screen, BLACK, (player[0], player[1]), 20, 3)

def draw_all_circals(player1, player2, player3, player4):
    screen.blit(BACKGROUND, (0, 0))
    draw_player1(player1)
    draw_player2(player2)
    draw_player3(player3)
    draw_player4(player4)
    pygame.display.update()

def draw_movment1(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j*WIDTH/10 + WIDTH/10/2 - 10, i*HIGHT/10 + HIGHT/10/2
        while player1[0] != x or player1[1] != y:
            clock.tick(250)
            a = player1[1]//100
            if location != 100 and player1[0] == 50 and player1[1] == 50:
                while player1[0] != x or player1[1] != y:
                    player1[0] = player1[0] + 1
                    draw_all_circals(player1, player2, player3, player4)
            elif location > 100:
                player1[0] = 50
                player1[1] = 50
                break
            elif a % 2 != 0:
                if player1[0] == 940:
                    for i in range(100):
                        clock.tick(250)
                        player1[1] = player1[1] - 1
                        draw_all_circals(player1, player2, player3, player4)
                else:
                    player1[0] = player1[0] + 1
                    draw_all_circals(player1, player2, player3, player4)
            else:
                if player1[0] == 40:
                    for i in range(100):
                        clock.tick(250)
                        player1[1] = player1[1] - 1
                        draw_all_circals(player1, player2, player3, player4)
                else:
                    player1[0] = player1[0] - 1
                    draw_all_circals(player1, player2, player3, player4)

def draw_movment2(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH / 10 + WIDTH / 10 / 2 - 2, i * HIGHT / 10 + HIGHT / 10 / 2
        while player1[0] != x or player1[1] != y:
            clock.tick(250)
            a = player1[1]//100
            if location != 100 and player1[0] == 50 and player1[1] == 50:
                while player1[0] != x or player1[1] != y:
                    player1[0] = player1[0] + 1
                    draw_all_circals(player2, player1, player3, player4)
            elif location > 100:
                player1[0] = 50
                player1[1] = 50
                break
            elif a % 2 != 0:
                if player1[0] == 948:
                    for i in range(100):
                        clock.tick(250)
                        player1[1] = player1[1] - 1
                        draw_all_circals(player2, player1, player3, player4)
                else:
                    player1[0] = player1[0] + 1
                    draw_all_circals(player2, player1, player3, player4)
            else:
                if player1[0] == 48:
                    for i in range(100):
                        clock.tick(250)
                        player1[1] = player1[1] - 1
                        draw_all_circals(player2, player1, player3, player4)
                else:
                    player1[0] = player1[0] - 1
                    draw_all_circals(player2, player1, player3, player4)

def draw_movment3(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH / 10 + WIDTH / 10 / 2 + 6, i * HIGHT / 10 + HIGHT / 10 / 2
        while player1[0] != x or player1[1] != y:
            clock.tick(250)
            a = player1[1]//100
            if location != 100 and player1[0] == 50 and player1[1] == 50:
                while player1[0] != x or player1[1] != y:
                    player1[0] = player1[0] + 1
                    draw_all_circals(player3, player2, player1, player4)
            elif location > 100:
                player1[0] = 50
                player1[1] = 50
                break
            elif a % 2 != 0:
                if player1[0] == 956:
                    for i in range(100):
                        clock.tick(250)
                        player1[1] = player1[1] - 1
                        draw_all_circals(player3, player2, player1, player4)
                else:
                    player1[0] = player1[0] + 1
                    draw_all_circals(player3, player2, player1, player4)
            else:
                if player1[0] == 56:
                    for i in range(100):
                        clock.tick(250)
                        player1[1] = player1[1] - 1
                        draw_all_circals(player3, player2, player1, player4)
                else:
                    player1[0] = player1[0] - 1
                    draw_all_circals(player3, player2, player1, player4)

def draw_movment4(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH/10 + WIDTH/10/2 + 14, i*HIGHT/10 + HIGHT/10/2
        while player1[0] != x or player1[1] != y:
            clock.tick(250)
            a = player1[1]//100
            if location != 100 and player1[0] == 50 and player1[1] == 50:
                while player1[0] != x or player1[1] != y:
                    player1[0] = player1[0] + 1
                    draw_all_circals(player4, player2, player3, player1)
            elif location > 100:
                player1[0] = 50
                player1[1] = 50
                break
            elif a % 2 != 0:
                if player1[0] == 964:
                    for i in range(100):
                        clock.tick(250)
                        player1[1] = player1[1] - 1
                        draw_all_circals(player4, player2, player3, player1)
                else:
                    player1[0] = player1[0] + 1
                    draw_all_circals(player4, player2, player3, player1)
            else:
                if player1[0] == 64:
                    for i in range(100):
                        clock.tick(250)
                        player1[1] = player1[1] - 1
                        draw_all_circals(player4, player2, player3, player1)
                else:
                    player1[0] = player1[0] - 1
                    draw_all_circals(player4, player2, player3, player1)

def ladders_climb1(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH/10 + WIDTH/10/2 - 10, i*HIGHT/10 + HIGHT/10/2
        if player1[0] != x:
            m = (player1[1] - y) / (player1[0] - x)
            while player1[0] != x or player1[1] != y:
                clock.tick(250)
                if m > 0:
                    player1[0] = player1[0] - 1
                    player1[1] = player1[1] - m
                    draw_all_circals(player1, player2, player3, player4)
                    if player1[0] < x and player1[1] < y:
                        player1[0] = x
                        player1[1] = y

                else:
                    player1[0] = player1[0] + 1
                    player1[1] = player1[1] + m
                    draw_all_circals(player1, player2, player3, player4)
                    if player1[0] > x and player1[1] < y:
                        player1[0] = x
                        player1[1] = y
        else:
            while player1[1] != y:
                player1[1] = player1[1] - 1
                if player1[1] < y:
                    player1[1] = y
                draw_all_circals(player1, player2, player3, player4)

def ladders_climb2(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH/10 + WIDTH/10/2 - 2, i*HIGHT/10 + HIGHT/10/2
        if player1[0] != x:
            m = (player1[1] - y) / (player1[0] - x)
            while player1[0] != x or player1[1] != y:
                clock.tick(250)
                if m > 0:
                    player1[0] = player1[0] - 1
                    player1[1] = player1[1] - m
                    draw_all_circals(player2, player1, player3, player4)
                    if player1[0] < x and player1[1] < y:
                        player1[0] = x
                        player1[1] = y
                else:
                    player1[0] = player1[0] + 1
                    player1[1] = player1[1] + m
                    draw_all_circals(player2, player1, player3, player4)
                    if player1[0] > x and player1[1] < y:
                        player1[0] = x
                        player1[1] = y
        else:
            while player1[1] != y:
                player1[1] = player1[1] - 1
                if player1[1] < y:
                    player1[1] = y
                draw_all_circals(player2, player1, player3, player4)

def ladders_climb3(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH/10 + WIDTH/10/2 + 6, i*HIGHT/10 + HIGHT/10/2
        if player1[0] != x:
            m = (player1[1] - y) / (player1[0] - x)
            while player1[0] != x or player1[1] != y:
                clock.tick(250)
                if m > 0:
                    player1[0] = player1[0] - 1
                    player1[1] = player1[1] - m
                    draw_all_circals(player3, player2, player1, player4)
                    if player1[0] < x and player1[1] < y:
                        player1[0] = x
                        player1[1] = y
                else:
                    player1[0] = player1[0] + 1
                    player1[1] = player1[1] + m
                    draw_all_circals(player3, player2, player1, player4)
                    if player1[0] > x and player1[1] < y:
                        player1[0] = x
                        player1[1] = y
        else:
            while player1[1] != y:
                player1[1] = player1[1] - 1
                if player1[1] < y:
                    player1[1] = y
                draw_all_circals(player3, player2, player1, player4)

def ladders_climb4(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH/10 + WIDTH/10/2 + 14, i*HIGHT/10 + HIGHT/10/2
        if player1[0] != x:
            m = (player1[1] - y) / (player1[0] - x)
            while player1[0] != x or player1[1] != y:
                clock.tick(250)
                if m > 0:
                    player1[0] = player1[0] - 1
                    player1[1] = player1[1] - m
                    draw_all_circals(player4, player2, player3, player1)
                    if player1[0] < x and player1[1] < y:
                        player1[0] = x
                        player1[1] = y
                else:
                    player1[0] = player1[0] + 1
                    player1[1] = player1[1] + m
                    draw_all_circals(player4, player2, player3, player1)
                    if player1[0] > x and player1[1] < y:
                        player1[0] = x
                        player1[1] = y
        else:
            while player1[1] != y:
                player1[1] = player1[1] - 1
                if player1[1] < y:
                    player1[1] = y
                draw_all_circals(player4, player2, player3, player1)

def snakes_climb1(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH / 10 + WIDTH / 10 / 2 - 10, i * HIGHT / 10 + HIGHT / 10 / 2
        if player1[0] != x:
            m = (player1[1] - y) / (player1[0] - x)
            while player1[0] != x or player1[1] != y:
                clock.tick(250)
                if m > 0:
                    player1[0] = player1[0] + 1
                    player1[1] = player1[1] + m
                    draw_all_circals(player1, player2, player3, player4)
                    if player1[0] > x and player1[1] > y:
                        player1[0] = x
                        player1[1] = y
                else:
                    player1[0] = player1[0] - 1
                    player1[1] = player1[1] - m
                    draw_all_circals(player1, player2, player3, player4)
                    if player1[0] < x and player1[1] > y:
                        player1[0] = x
                        player1[1] = y
        else:
            while player1[1] != y:
                player1[1] = player1[1] + 1
                if player1[1] > y:
                    player1[1] = y
                draw_all_circals(player1, player2, player3, player4)

def snakes_climb2(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH / 10 + WIDTH / 10 / 2 - 2, i * HIGHT / 10 + HIGHT / 10 / 2
        if player1[0] != x:
            m = (player1[1] - y) / (player1[0] - x)
            while player1[0] != x or player1[1] != y:
                clock.tick(250)
                if m > 0:
                    player1[0] = player1[0] + 1
                    player1[1] = player1[1] + m
                    draw_all_circals(player2, player1, player3, player4)
                    if player1[0] > x and player1[1] > y:
                        player1[0] = x
                        player1[1] = y
                else:
                    player1[0] = player1[0] - 1
                    player1[1] = player1[1] - m
                    draw_all_circals(player2, player1, player3, player4)
                    if player1[0] < x and player1[1] > y:
                        player1[0] = x
                        player1[1] = y
        else:
            while player1[1] != y:
                player1[1] = player1[1] + 1
                if player1[1] > y:
                    player1[1] = y
                draw_all_circals(player2, player1, player3, player4)

def snakes_climb3(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH / 10 + WIDTH / 10 / 2 + 6, i * HIGHT / 10 + HIGHT / 10 / 2
        if player1[0] != x:
            m = (player1[1] - y) / (player1[0] - x)
            while player1[0] != x or player1[1] != y:
                clock.tick(250)
                if m > 0:
                    player1[0] = player1[0] + 1
                    player1[1] = player1[1] + m
                    draw_all_circals(player3, player2, player1, player4)
                    if player1[0] > x and player1[1] > y:
                        player1[0] = x
                        player1[1] = y
                else:
                    player1[0] = player1[0] - 1
                    player1[1] = player1[1] - m
                    draw_all_circals(player3, player2, player1, player4)
                    if player1[0] < x and player1[1] > y:
                        player1[0] = x
                        player1[1] = y
        else:
            while player1[1] != y:
                player1[1] = player1[1] + 1
                if player1[1] > y:
                    player1[1] = y
                draw_all_circals(player3, player2, player1, player4)

def snakes_climb4(player1, player2, player3, player4, location):
    clock = pygame.time.Clock()
    if identify_location(location):
        i, j = identify_location2(location)
        x, y = j * WIDTH / 10 + WIDTH / 10 / 2 + 14, i * HIGHT / 10 + HIGHT / 10 / 2
        if player1[0] != x:
            m = (player1[1] - y) / (player1[0] - x)
            while player1[0] != x or player1[1] != y:
                clock.tick(250)
                if m > 0:
                    player1[0] = player1[0] + 1
                    player1[1] = player1[1] + m
                    draw_all_circals(player4, player2, player3, player1)
                    if player1[0] > x and player1[1] > y:
                        player1[0] = x
                        player1[1] = y
                else:
                    player1[0] = player1[0] - 1
                    player1[1] = player1[1] - m
                    draw_all_circals(player4, player2, player3, player1)
                    if player1[0] < x and player1[1] > y:
                        player1[0] = x
                        player1[1] = y
        else:
            while player1[1] != y:
                player1[1] = player1[1] + 1
                if player1[1] > y:
                    player1[1] = y
                draw_all_circals(player4, player2, player3, player1)

def snakes_program(location):
    for i in range(8):
        if location == list(snakes)[i]:
            return True
    return False

def snakes_program2(location):
    for i in range(8):
        if location == list(snakes)[i]:
            return snakes[list(snakes)[i]]

def ladders_program(location):
    for i in range(8):
        if location == list(ladders)[i]:
            return True
    return False

def ladders_program2(location):
    for i in range(8):
        if location == list(ladders)[i]:
            return ladders[list(ladders)[i]]


def if_bigger_then_100(location, num):
    if location + num > 100:
       return 100 - (location + num - 100)

def if_bigger_then_100_bool(location, num):
    if location + num > 100:
       return True

def main():
    run = True
    clock = pygame.time.Clock()
    player = 1
    player1 = [-20, 950]
    player2 = [-20, 950]
    player3 = [-20, 950]
    player4 = [-20, 950]
    player1_location = 0
    player2_location = 0
    player3_location = 0
    player4_location = 0
    player1_location_2 = 0
    player2_location_2 = 0
    player3_location_2 = 0
    player4_location_2 = 0
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                num = random.randint(1, 6)
                if num == 1:
                    screen.blit(DICE_1, (1050, 159*5))
                elif num == 2:
                    screen.blit(DICE_2, (1050, 159 * 5))
                elif num == 3:
                    screen.blit(DICE_3, (1050, 159 * 5))
                elif num == 4:
                    screen.blit(DICE_4, (1050, 159 * 5))
                elif num == 5:
                    screen.blit(DICE_5, (1050, 159 * 5))
                elif num == 6:
                    screen.blit(DICE_6, (1050, 159 * 5))
                if player == 1:
                    if if_bigger_then_100_bool(player1_location, num):
                        player1_location_2 = if_bigger_then_100(player1_location, num)
                    if snakes_program(player1_location + num):
                        draw_movment1(player1, player2, player3, player4, player1_location + num)
                        player1_location = snakes_program2(player1_location + num)
                        snakes_climb1(player1, player2, player3, player4, player1_location)
                    elif ladders_program(player1_location + num):
                        draw_movment1(player1, player2, player3, player4, player1_location + num)
                        player1_location = ladders_program2(player1_location + num)
                        ladders_climb1(player1, player2, player3, player4, player1_location)
                    else:
                        player1_location = player1_location + num
                        draw_movment1(player1, player2, player3, player4, player1_location)
                    if player1_location_2 > 100:
                        draw_movment1(player1, player2, player3, player4, player1_location_2)
                    pygame.draw.rect(screen, PURPLE, (1000, 0, 200, 250))
                    font = pygame.font.Font('freesansbold.ttf', 29)
                    font_text = font.render("RED [ " + str(player1_location) + " ]", 1, RED)
                    screen.blit(font_text, (1020, 159))
                    pygame.display.update()
                    player = 2
                elif player == 2:
                    if if_bigger_then_100_bool(player2_location, num):
                        player2_location_2 = if_bigger_then_100(player2_location, num)
                    if snakes_program(player2_location + num):
                        draw_movment2(player2, player1, player3, player4, player2_location + num)
                        player2_location = snakes_program2(player2_location + num)
                        snakes_climb2(player2, player1, player3, player4, player2_location)
                    elif ladders_program(player2_location + num):
                        draw_movment2(player2, player1, player3, player4, player2_location + num)
                        player2_location = ladders_program2(player2_location + num)
                        ladders_climb2(player2, player1, player3, player4, player2_location)
                    else:
                        player2_location = player2_location + num
                        draw_movment2(player2, player1, player3, player4, player2_location)
                    if player2_location_2 > 100:
                        draw_movment2(player2, player1, player3, player4, player2_location_2)
                    pygame.draw.rect(screen, PURPLE, (1000, 250, 200, 150))
                    font = pygame.font.Font('freesansbold.ttf', 26)
                    font_text = font.render("YELLOW [ " + str(player2_location) + " ]", 1, YELLOW)
                    screen.blit(font_text, (1010, 159*2))
                    pygame.display.update()
                    player = 3
                elif player == 3:
                    if if_bigger_then_100_bool(player3_location, num):
                        player3_location_2 = if_bigger_then_100(player3_location, num)
                    if snakes_program(player3_location + num):
                        draw_movment3(player3, player2, player1, player4, player3_location + num)
                        player3_location = snakes_program2(player3_location + num)
                        snakes_climb3(player3, player2, player1, player4, player3_location)
                    elif ladders_program(player3_location + num):
                        draw_movment3(player3, player2, player1, player4, player3_location + num)
                        player3_location = ladders_program2(player3_location + num)
                        ladders_climb3(player3, player2, player1, player4, player3_location)
                    else:
                        player3_location = player3_location + num
                        draw_movment3(player3, player2, player1, player4, player3_location)
                    if player3_location_2 > 100:
                        draw_movment3(player3, player2, player1, player4, player3_location_2)
                    pygame.draw.rect(screen, PURPLE, (1000, 400, 200, 200))
                    font = pygame.font.Font('freesansbold.ttf', 29)
                    font_text = font.render("GREEN [ " + str(player3_location) + " ]", 1, GREEN)
                    screen.blit(font_text, (1015, 159*3))
                    pygame.display.update()
                    player = 4
                elif player == 4:
                    if if_bigger_then_100_bool(player4_location, num):
                        player4_location_2 = if_bigger_then_100(player4_location, num)
                    if snakes_program(player4_location + num):
                        draw_movment4(player4, player2, player3, player1, player4_location + num)
                        player4_location = snakes_program2(player4_location + num)
                        snakes_climb4(player4, player2, player3, player1, player4_location)
                    elif ladders_program(player4_location + num):
                        draw_movment4(player4, player2, player3, player1, player4_location + num)
                        player4_location = ladders_program2(player4_location + num)
                        ladders_climb4(player4, player2, player3, player1, player4_location)
                    else:
                        player4_location = player4_location + num
                        draw_movment4(player4, player2, player3, player1, player4_location)
                    if player4_location_2 > 100:
                        draw_movment4(player4, player2, player3, player1, player4_location_2)
                    pygame.draw.rect(screen, PURPLE, (1000, 600, 200, 150))
                    font = pygame.font.Font('freesansbold.ttf', 29)
                    font_text = font.render("BLUE [ " + str(player4_location) + " ]", 1, LIGHT_BLUE)
                    screen.blit(font_text, (1020, 159*4))
                    pygame.display.update()
                    player = 1
        if player1_location == 100 or player2_location == 100 or player3_location == 100 or player4_location == 100:
            run = False






if __name__ == "__main__":
    main()
