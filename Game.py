import pygame

pygame.display.init()

def main():

    WINDOW_WIDTH = 800
    WINDOW_LENGTH = 1000

    GUI = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_LENGTH))
    pygame.display.set_caption("SpaceShooter")
    run = True

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        GUI.fill((40, 40, 40))
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()
    pygame.quit()
