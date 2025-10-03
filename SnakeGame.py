import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((1200, 900))

#Main game loop
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
              

    # Draw all the elements here
    pygame.display.update()