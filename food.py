import pygame
import random
import math

color = (255, 0, 0)
radius = 10
speed = 1
cd = 100
GREEN = (0, 255, 0)
size = 3


class Food:

    def __init__(self, master, x, y):
        self._master = master
        self.x = x
        self.y = y
        self.lives = 1

    def update(self):
        temp = random.randint(0, 3)
        if temp == 0:
            self.y += speed
            self.x += speed
        if temp == 1:
            self.y += speed
            self.x -= speed
        if temp == 2:
            self.y -= speed
            self.x -= speed
        if temp == 3:
            self.y -= speed
            self.x += speed

    def draw(self):
        x = self.x
        y = self.y
        point1 = [(x - math.sqrt(3) * size), (y - size)]
        point2 = [(x + math.sqrt(3) * size), (y - size)]
        point3 = [x, (y + 2 * size)]
        pygame.draw.polygon(self._master, GREEN, [point1, point2, point3], size)

    def get_center(self):
        return self.x, self.y

    def get_radius(self):
        return size


class Food_move:
    def __init__(self, master):
        self._master = master
        self.food_list = []
        self.time = 0
        self.num = 0
        self.lives = 1

    def number(self):
        self.time += 1
        if self.time % cd == 0:
            x_scale = random.randint(0, self._master.get_width() - radius * 2)
            y_scale = random.randint(0, self._master.get_width() - radius * 2)
            z = Food(self._master, x_scale, y_scale)
            self.food_list.append(z)
            self.num += 1

    def update(self):
        temp = []
        for food in self.food_list:
            food.update()
            if food.lives>0:
                temp.append(food)
            self.food_list = temp

    def draw(self):
        for food in self.food_list:
            food.draw()
