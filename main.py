import pygame
import sys
import os
from player import Player
from obstacle import ObstacleM
from food import Food
from food import Food_move

worldx = 960
worldy = 720
fps = 60
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
    clock.tick(fps)
    pygame.display.flip()
