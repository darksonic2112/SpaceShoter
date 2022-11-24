import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption("SpaceShooter")

def main():

    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 1000

    SHIP_WIDTH = 25
    SHIP_HEIGHT = 50
    SHIP_POS_X = 330
    SHIP_POS_Y = 850
    SHIP_VELOCITY = 0.3

    PROJECTILE_WIDTH = 5
    PROJECTILE_HEIGHT = 10
    PROJECTILE_POS_X = SHIP_POS_X
    PROJECTILE_POS_Y = SHIP_POS_Y
    PROJECTILE_VELOCITY = 0.6

    BACKGROUND = (40, 40, 40)
    GUI = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
    GUI.fill(BACKGROUND) # Dark grey

    clock = pygame.time.Clock()


    running = True

    # Event loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        
        PROJECTILE_POS_Y += PROJECTILE_VELOCITY


        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and SHIP_POS_X > 0:
                SHIP_POS_X -= SHIP_VELOCITY
            
        if keys[pygame.K_RIGHT] and SHIP_POS_X < (WINDOW_WIDTH - SHIP_WIDTH):
                SHIP_POS_X += SHIP_VELOCITY

        if keys[pygame.K_UP] and SHIP_POS_Y > 0:
                SHIP_POS_Y -= SHIP_VELOCITY

        if keys[pygame.K_DOWN] and SHIP_POS_Y < (WINDOW_HEIGHT - (SHIP_HEIGHT/2)):
                SHIP_POS_Y += SHIP_VELOCITY

        GUI.fill(BACKGROUND)
        SHIP = pygame.draw.rect(GUI, (255,255,255), (SHIP_POS_X, SHIP_POS_Y, SHIP_WIDTH, SHIP_HEIGHT))
        PROJECTILE = pygame.draw.rect(GUI, (255,255,255), (SHIP_POS_X, (SHIP_POS_Y + 1), PROJECTILE_WIDTH, PROJECTILE_HEIGHT))
        
        pygame.display.update()
    
    
    pygame.quit()
    
if __name__ == '__main__':
    main()
    pygame.quit()
