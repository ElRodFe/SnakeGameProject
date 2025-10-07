import pygame
import sys

pygame.init()

    ###Game program elements
screen = pygame.display.set_mode((1200, 900))
clock = pygame.time.Clock()
grass_color = (51, 102, 0)

#Snake element
snake_color = (102, 0, 0)
snake = pygame.Surface((100, 200))
snake_xpos = 600
snake_ypos = 450
snake.fill(snake_color)

#Main game loop
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()

    #Draw game here
    screen.fill(grass_color)
    screen.blit(snake, (snake_xpos, snake_ypos))

    pygame.display.update()
    clock.tick(60)