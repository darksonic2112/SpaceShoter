import pygame

pygame.display.init()

def main():

    WINDOW_WIDTH = 800
    WINDOW_LENGTH = 1000

    GUI = pygame.display.set_mode(size=(WINDOW_WIDTH, WINDOW_LENGTH))
    pygame.display.set_caption("SpaceShooter")
    running = True
    GUI.fill((40, 40, 40))
    pygame.display.update()

    while running:

        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    background = (0,0,0)
                elif event.key == pygame.K_g:
                    background = (255,255,255)

                GUI.fill(background)
                pygame.display.update()

    pygame.quit()
    
if __name__ == '__main__':
    main()
    pygame.quit()
