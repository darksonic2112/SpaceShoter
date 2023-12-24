import pygame

pygame.init()

win = pygame.display.set_mode((800, 1000))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

SHIP_WIDTH = 25
SHIP_HEIGHT = 50
SHIP_POS_X = 330
SHIP_POS_Y = 850
SHIP_VELOCITY = 1


def redraw_game_window():
    win.fill((40, 40, 40))
    pygame.draw.rect(win, (255, 255, 255), (SHIP_POS_X, SHIP_POS_Y, SHIP_WIDTH, SHIP_HEIGHT))
    pygame.display.update()


run = True
while run:
    clock.tick(240)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and SHIP_POS_X > 0:
        SHIP_POS_X -= SHIP_VELOCITY

    if keys[pygame.K_RIGHT] and SHIP_POS_X < (800 - SHIP_WIDTH):
        SHIP_POS_X += SHIP_VELOCITY

    if keys[pygame.K_UP] and SHIP_POS_Y > 0:
        SHIP_POS_Y -= SHIP_VELOCITY

    if keys[pygame.K_DOWN] and SHIP_POS_Y < (1000 - (SHIP_HEIGHT / 2)):
        SHIP_POS_Y += SHIP_VELOCITY

    redraw_game_window()

pygame.quit()
