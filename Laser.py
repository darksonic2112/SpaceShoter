import pygame


class Laser:
    def __init__(self, x, y):
        super().__init__()
        self.rect = pygame.Rect(x, y, 10, 20)
