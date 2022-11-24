import pygame

class Ship:
    def __init__(self) -> None:
        pass
    SHIP_WIDTH = 25
    SHIP_HEIGHT = 50
    SHIP_POS_X = 330
    SHIP_POS_Y = 850
    VELOCITY = 0.3

    SHIP = pygame.draw.rect(GUI, (255,255,255), (SHIP_POS_X, SHIP_POS_Y, SHIP_WIDTH, SHIP_HEIGHT))