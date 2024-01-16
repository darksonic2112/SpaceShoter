import pygame
import random


class SpaceShip:

    def __init__(self):
        self.SPACESHIP_GRAPHIC = pygame.image.load("upgrade.png")
        self.WIDTH = 10
        self.HEIGHT = 10
        self.pos_x = random.randrange(50, 950, 50)
        self.pos_y = -50

        self.HITBOX = (self.pos_x + 5, self.pos_y + 5, self.WIDTH, self.HEIGHT)
