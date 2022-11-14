import pygame
from pygame.locals import *

pygame.display.init()

def main():

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 1000

    SHIP_WIDTH = 50
    SHIP_HEIGHT = 100
    SHIP_START_POS_X = 325
    SHIP_START_POS_Y = 850

    GUI = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("SpaceShooter")
    running = True
    background = (40, 40, 40)
    GUI.fill(background) # Dark grey
    SHIP = pygame.draw.rect(GUI, (255,255,255), (SHIP_START_POS_X, SHIP_START_POS_Y, SHIP_WIDTH, SHIP_HEIGHT))
    pygame.display.update()
    mouse_position = pygame.mouse.get_pos()
    moving = False

    # Event loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == MOUSEMOTION:
                SHIP.move_ip(event.rel)
            

       
            pygame.display.update()

    pygame.quit()
    
if __name__ == '__main__':
    main()
    pygame.quit()
