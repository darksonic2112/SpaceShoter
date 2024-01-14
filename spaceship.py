import pygame


class SpaceShip:

    def __init__(self):
        self.SPACESHIP_GRAPHIC = pygame.image.load("Space_Ship.png")
        self.SHIP_WIDTH = 16
        self.SHIP_HEIGHT = 20
        self.ship_pos_x = 330
        self.ship_pos_y = 850
        self.ship_velocity = 1.66

        self.HITBOX = (self.ship_pos_x + 8, self.ship_pos_y + 10, self.SHIP_WIDTH, self.SHIP_HEIGHT)

