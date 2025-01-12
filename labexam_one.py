import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *  


def draw_triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(0.5, 0, 0.5)  
    glVertex2f(0.0, 1.0)
    glVertex2f(-1.0, -1.0)
    glVertex2f(1.0, -1.0)
    glEnd()


def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluOrtho2D(-2, 2, -2, 2)  
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_triangle()
        pygame.display.flip()
        pygame.time.wait(10)
    
    pygame.quit()


if __name__ == "__main__":
    main()


