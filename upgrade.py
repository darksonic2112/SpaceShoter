import pygame
import random


class Upgrade:

    def __init__(self):
        self.UPGRADE_GRAPHIC = pygame.image.load("upgrade.png")
        self.WIDTH = 10
        self.HEIGHT = 10
        self.pos_x = 0
        self.pos_y = -50
        self.descent_speed = 5

        self.HITBOX = (self.pos_x + 5, self.pos_y + 5, self.WIDTH, self.HEIGHT)
