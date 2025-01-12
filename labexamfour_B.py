import pygame
import sys

def main():
 
    pygame.init()

    
    width, height = 500, 400
    screen = pygame.display.set_mode((width, height))


    pygame.display.set_caption("My Pygame Canvas")

   
    screen.fill((255, 255, 255))

    
    start_pos = (50, 50)
    end_pos = (start_pos[0] + 200, start_pos[1])  
    line_color = (255, 0, 0)  
    line_width = 3

    pygame.draw.line(screen, line_color, start_pos, end_pos, line_width)

  
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