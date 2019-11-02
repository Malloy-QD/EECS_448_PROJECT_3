import pygame
import random

color = (255, 0, 0)
radius = 10
speed = 1
cd = 100


class Obstacle:

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
        pygame.draw.circle(self._master, color, (self.x, self.y), radius)

    def get_center(self):
        return self.x + radius / 2, self.y + radius / 2

    def get_radius(self):
        return radius / 2


class ObstacleM:
    def __init__(self, master):
        self._master = master
        self.list = []
        self.time = 0
        self.num = 0
        self.lives = 1

    def number(self):
        self.time += 1
        if self.time % cd == 0:
            x_scale = random.randint(0, self._master.get_width() - radius * 2)
            y_scale = random.randint(0, self._master.get_width() - radius * 2)
            z = Obstacle(self._master, x_scale, y_scale)
            self.list.append(z)
            self.num += 1

    def update(self):
        temp = []
        for obstacle in self.list:
            obstacle.update()
            temp.append(obstacle)
            self.list = temp

    def draw(self):
        for obstacle in self.list:
            obstacle.draw()
