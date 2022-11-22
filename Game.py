import pygame
from pygame.locals import *

pygame.display.init()

def main():

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 1000

    SHIP_WIDTH = 25
    SHIP_HEIGHT = 50
    SHIP_POS_X = 330
    SHIP_POS_Y = 850
    VELOCITY = 0.3

    GUI = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("SpaceShooter")
    running = True
    BACKGROUND = (40, 40, 40)
    GUI.fill(BACKGROUND) # Dark grey
    pygame.display.update()
    mouse_position = pygame.mouse.get_pos()
    moving = False

    # Event loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and SHIP_POS_X > 0:
                SHIP_POS_X -= VELOCITY
            
        if keys[pygame.K_RIGHT] and SHIP_POS_X < (WINDOW_WIDTH - SHIP_WIDTH):
                SHIP_POS_X += VELOCITY

        if keys[pygame.K_UP] and SHIP_POS_Y > 0:
                SHIP_POS_Y -= VELOCITY

        if keys[pygame.K_DOWN] and SHIP_POS_Y < (WINDOW_HEIGHT - (SHIP_HEIGHT/2)):
                SHIP_POS_Y += VELOCITY
       
        GUI.fill(BACKGROUND)
        SHIP = pygame.draw.rect(GUI, (255,255,255), (SHIP_POS_X, SHIP_POS_Y, SHIP_WIDTH, SHIP_HEIGHT))
        pygame.display.update()
    
    
    pygame.quit()
    
if __name__ == '__main__':
    main()
    pygame.quit()
