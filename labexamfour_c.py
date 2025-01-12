import pygame
import sys


pygame.init()


width, height = 400, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Entangled Triangles")


blue = (0, 0, 255)
white = (255, 255, 255)

def draw_triangles(screen):
   
    outer_triangle = [(200, 50), (100, 300), (300, 300)]
    
    inner_triangle = [(150, 200), (250, 200), (200, 300)]
    
    
    pygame.draw.polygon(screen, blue, outer_triangle)
    
    pygame.draw.polygon(screen, white, inner_triangle)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

   
    screen.fill(white)
    
 
    draw_triangles(screen)

  
    pygame.display.flip()