import pygame
import sys
import os
from player import Player
from obstacle import ObstacleM
from food import Food
from food import Food_move

worldx = 960
worldy = 720
fps = 144
level = 1
clock = pygame.time.Clock()
main = True

pygame.init()

back = 'image/backbord.jpg'
shark = 'image/icon.png'

screen = pygame.display.set_mode((worldx, worldy))
background = pygame.image.load(back).convert()
background = pygame.transform.scale(background, (worldx, worldy), screen)
player = Player(background, 200, 200, shark)
om = ObstacleM(background)
fm = Food_move(background)
mx = 0
my = 0
speed = 3
count = 0
fonts = {
    16: pygame.font.SysFont("Times New Roman", 16, True),
    32: pygame.font.SysFont("Times New Roman", 32, True)
}


def get_level():
    global level
    if player.score == level * 5:
        level += 1
        reset_game()
    return level


def reset_game():
    player.score = 0


def draw():
    score = fonts[16].render("Scores: " + str(max([player.score, 0])), True, (0, 0, 0))
    screen.blit(score, (10, 25))
    level = fonts[16].render("Level: " + str(get_level()), True, (0, 0, 0))
    screen.blit(level, (10, 10))
    next_level = fonts[16].render("Get into Next Level Needs to Score " + str(5*get_level() - max([player.score, 0])) + " More Points",
                                  True, (0, 0, 0))
    screen.blit(next_level, (10, 40))
    pygame.display.flip()


while main == True:
    background = pygame.image.load(back).convert()
    background = pygame.transform.scale(background, (worldx, worldy), screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                sys.exit()
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('a'):
                mx = -speed
            if event.key == ord('w'):
                my = -speed
            if event.key == ord('d'):
                mx = speed
            if event.key == ord('s'):
                my = speed
        if event.type == pygame.KEYUP:
            if event.key == ord('a'):
                if mx == -speed:
                    my = 0
            if event.key == ord('w'):
                if my == -speed:
                    mx = 0
            if event.key == ord('d'):
                if mx == speed:
                    my = 0
            if event.key == ord('s'):
                if my == speed:
                    mx = 0
    player.check_status(om.list)
    if player.lives <= 0:
        print("You lose your shark!")
        break
    player.check_food(fm.food_list)
    om.number()
    om.update()
    om.draw()

    fm.number()
    fm.update()
    fm.draw()

    player.move(mx, my)
    player.draw()
    draw()
    dt = 1.0 / float(fps)
    clock.tick(fps)
    pygame.display.flip()
