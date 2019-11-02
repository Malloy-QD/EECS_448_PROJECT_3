import pygame
import math
import sys
from obstacle import Obstacle
from obstacle import ObstacleM
from food import Food_move
from food import Food

sharksize = 30
color = (0, 0, 0)


class Player:

    def __init__(self, master, x, y, img_path):
        self._master = master
        self.image = pygame.image.load(img_path)
        self.x = x
        self.y = y
        self.lives = 1
        self.score = 0

    def move(self, x, y):
        if 0 < self.x + sharksize / 2 + x <= self._master.get_width():
            self.x += x
        if 0 < self.y + sharksize / 2 + y <= self._master.get_height():
            self.y += y

    def draw(self):
        pygame.draw.circle(self._master, color, (self.x, self.y), sharksize)

    def get_center(self):
        return self.x + sharksize / 2, self.y + sharksize / 2

    def get_distance(self, xy):
        x, y = xy
        x_distance = self.x + sharksize / 2
        y_distance = self.y + sharksize / 2
        return math.sqrt(math.pow(x_distance - x, 2) + (math.pow(y_distance - y, 2)))

    def check_status(self, list):
        for i in list:
            if i.lives > 0:
                temp = self.get_distance(i.get_center())
                if temp <= sharksize / 2 + i.get_radius():
                    self.lives = 0
                    i.lives = 0

    def check_food(self, food_list):
        for j in food_list:
            if j.lives > 0:
                temp = self.get_distance(j.get_center())
                if temp <= sharksize / 2 + j.get_radius():
                    self.lives = 1
                    self.score += 1
                    j.lives = 0
