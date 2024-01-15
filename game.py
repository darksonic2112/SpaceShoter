import pygame
from spaceship import SpaceShip
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


def shooting(missile_position_x, missile_position_y):
    missile_speed = 50
    missile = pygame.Rect(missile_position_x + 8, missile_position_y, 5, 40)
    missile_1 = pygame.Rect(missile_position_x + 8, missile_position_y, 5, 40)#
    missile_2 = pygame.Rect(missile_position_x + 8, missile_position_y, 5, 40)

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


def redraw_game_window():
    window.fill(GREY)
    pygame.draw.rect(window, (0, 0, 0), ship.HITBOX)
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
        x = threading.Thread(target=shooting, args=(ship.ship_pos_x, ship.ship_pos_y))
        x.start()

    redraw_game_window()

pygame.quit()
