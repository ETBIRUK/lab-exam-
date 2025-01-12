import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

def draw_triangle():
    pygame.init()
    display = (500, 500)
    pygame.display.set_mode(display, pygame.DOUBLEBUF | pygame.OPENGL)


    glClearColor(0.0, 0.0, 0.0, 1.0)  
    gluOrtho2D(0, 500, 0, 500)  

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        glClear(GL_COLOR_BUFFER_BIT)  

        glColor3f(0.5, 0.0, 0.5)  
        glBegin(GL_TRIANGLES)
        glVertex2f(100, 100)
        glVertex2f(300, 100)
        glVertex2f(200, 300)
        glEnd()

        pygame.display.flip()  
        pygame.time.wait(10)  

    pygame.quit()

if __name__ == "__main__":
    draw_triangle()