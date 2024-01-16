import random

import pygame

import upgrade
from spaceship import SpaceShip
from upgrade import Upgrade
import threading

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 1000
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREY = (25, 25, 25)
BLACK = (0, 0, 0)

ship = SpaceShip()
upgrade = Upgrade()
upgrade_counter = 10


def shooting(missile_position_x, missile_position_y):
    missile_speed = 50
    missile = pygame.Rect(missile_position_x + 13, missile_position_y, 5, 40)
    missile_1 = pygame.Rect(missile_position_x + 13, missile_position_y, 5, 40)
    missile_2 = pygame.Rect(missile_position_x + 13, missile_position_y, 5, 40)

    while missile.y > -50:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        missile.y -= missile_speed
        missile_1.y -= missile_speed
        missile_1.x -= 4
        missile_2.y -= missile_speed
        missile_2.x += 4

        pygame.draw.rect(window, WHITE, missile)
        pygame.draw.rect(window, WHITE, missile_1)
        pygame.draw.rect(window, WHITE, missile_2)
        pygame.display.update()
        clock.tick(60)

        redraw_game_window()


def spawn_upgrade(x_position, y_position):
    upgrade = Upgrade()
    upgrade_box = pygame.Rect(x_position, y_position, upgrade.WIDTH, upgrade.HEIGHT)

    while y_position > WINDOW_HEIGHT - 10:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        upgrade_box += upgrade.descent_speed
        pygame.draw.rect(window, upgrade.UPGRADE_GRAPHIC, upgrade_box)
        pygame.display.update()
        clock.tick(60)
        redraw_game_window()


def redraw_game_window():
    window.fill(GREY)
    window.blit(ship.SPACESHIP_GRAPHIC, (ship.ship_pos_x, ship.ship_pos_y))
    pygame.display.update()


run = True
while run:
    clock.tick(240)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ship.ship_pos_x > 0:
        if keys[pygame.K_LSHIFT]:
            ship.ship_pos_x -= ship.ship_velocity / 3
        else:
            ship.ship_pos_x -= ship.ship_velocity

    if keys[pygame.K_RIGHT] and ship.ship_pos_x < (WINDOW_WIDTH - ship.SHIP_WIDTH * 2):
        if keys[pygame.K_LSHIFT]:
            ship.ship_pos_x += ship.ship_velocity / 3
        else:
            ship.ship_pos_x += ship.ship_velocity

    if keys[pygame.K_UP] and ship.ship_pos_y > 0:
        if keys[pygame.K_LSHIFT]:
            ship.ship_pos_y -= ship.ship_velocity / 3
        else:
            ship.ship_pos_y -= ship.ship_velocity

    if keys[pygame.K_DOWN] and ship.ship_pos_y < (1000 - 40):
        if keys[pygame.K_LSHIFT]:
            ship.ship_pos_y += ship.ship_velocity / 3
        else:
            ship.ship_pos_y += ship.ship_velocity

    if keys[pygame.K_SPACE]:
        shoot_thread = threading.Thread(target=shooting, args=(ship.ship_pos_x, ship.ship_pos_y))
        shoot_thread.start()

    spawn_upgrade(random.randrange(50, 550, 50), -50)

    redraw_game_window()

pygame.quit()
