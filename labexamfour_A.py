import pygame
import sys

def main():
   
    pygame.init()

    width, height = 500, 400
    screen = pygame.display.set_mode((width, height))

    pygame.display.set_caption("My Pygame Canvas")
    screen.fill((255, 255, 255))


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    main()