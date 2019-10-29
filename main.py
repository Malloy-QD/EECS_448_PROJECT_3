import pygame
import sys

pygame.display.init()
pygame.display.set_caption("ShakeShark")
surface = pygame.display.set_mode([500, 500])


def draw():
    surface.fill((0, 0, 0))
    pygame.display.flip()


if __name__ == "__main__":
    draw()
    pygame.quit()
