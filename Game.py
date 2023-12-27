import pygame

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 1000
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
GREY = (25, 25, 25)
BLACK = (0, 0, 0)

SPACESHIP_GRAPHIC = pygame.image.load("Space_Ship.png")
SPACESHIP_GRAPHIC_STANDARD = pygame.image.load("Space_Ship.png")
SPACESHIP_GRAPHIC_DOWN = pygame.image.load("Space_Ship_Backwards.png")

SHIP_WIDTH = 16
SHIP_HEIGHT = 20
ship_pos_x = 330
ship_pos_y = 850
SHIP_VELOCITY = 1.75
SHIP_COLOR = WHITE

HITBOX = (ship_pos_x + 8, ship_pos_y + 10, SHIP_WIDTH, SHIP_HEIGHT)


def ship_animation(direction="standard"):
    global SHIP_COLOR
    SHIP_COLOR = BLACK
    match direction:
        case "down":
            SPACESHIP_GRAPHIC = SPACESHIP_GRAPHIC_DOWN
        case "standard":
            window.blit(SPACESHIP_GRAPHIC_STANDARD, (ship_pos_x, ship_pos_y))


def redraw_game_window():
    global SPACESHIP_GRAPHIC
    window.fill(GREY)
    pygame.draw.rect(window, SHIP_COLOR, (ship_pos_x, ship_pos_y, SHIP_WIDTH, SHIP_HEIGHT))
    window.blit(SPACESHIP_GRAPHIC, (ship_pos_x, ship_pos_y))
    pygame.display.update()


run = True
while run:
    clock.tick(240)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and ship_pos_x > 0:
        if keys[pygame.K_LSHIFT]:
            ship_pos_x -= SHIP_VELOCITY / 3
            ship_animation()
        else:
            ship_pos_x -= SHIP_VELOCITY
            ship_animation()

    if keys[pygame.K_RIGHT] and ship_pos_x < (WINDOW_WIDTH - SHIP_WIDTH * 2):
        if keys[pygame.K_LSHIFT]:
            ship_pos_x += SHIP_VELOCITY / 3
            ship_animation()
        else:
            ship_pos_x += SHIP_VELOCITY
            ship_animation()

    if keys[pygame.K_UP] and ship_pos_y > 0:
        if keys[pygame.K_LSHIFT]:
            ship_pos_y -= SHIP_VELOCITY / 3
            ship_animation()
        else:
            ship_pos_y -= SHIP_VELOCITY
            ship_animation()

    if keys[pygame.K_DOWN] and ship_pos_y < (1000 - 40):
        if keys[pygame.K_LSHIFT]:
            ship_pos_y += SHIP_VELOCITY / 3
            ship_animation("down")
        else:
            ship_pos_y += SHIP_VELOCITY
            ship_animation("down")

    redraw_game_window()

pygame.quit()
