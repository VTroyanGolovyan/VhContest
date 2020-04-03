import pygame
import sys

#import Colors
#from Chart import Chart

FPS = 60
windowWidth = 900
windowHeight = 900
clock = pygame.time.Clock()

pygame.init()

canvas = pygame.display.set_mode((windowWidth, windowHeight))

#chart1 = Chart(canvas, x=100, y=100)
#chart1.draw()
pygame.display.update()

while 1:
    canvas.fill((0, 0, 0))
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #chart1.draw()
    pygame.draw.rect(canvas, (255, 255, 255), (300, 300, 300 + 60, 300 + 100))
    pygame.display.update()
    clock.tick(FPS)

