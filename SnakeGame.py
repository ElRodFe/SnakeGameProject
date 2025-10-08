import pygame
import sys
import random
from pygame.math import Vector2

#Create Snake class
class SNAKE:
     def __init__(self):
            self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]

     def draw_snake(self):
          #Positioning each "piece" of the snake
          for block in self.body:
               x_pos = block.x*cell_size
               y_pos = block.y*cell_size
               snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
               pygame.draw.rect(screen, (102, 0, 0), snake_rect)

#Create fruit class
class FRUIT:
     def __init__(self):
          #Random position for fruit every time the game starts
          self.x = random.randint(0, cell_number - 1)
          self.y = random.randint(0, cell_number - 1)
          self.pos = Vector2(self.x, self.y)
        
     def draw_fruit(self):
          fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
          pygame.draw.rect(screen, (255, 255, 51), fruit_rect)

pygame.init()

    ###Game program elements
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
grass_color = (51, 102, 0)

#Fruit and Snake elements
fruit = FRUIT()
snake = SNAKE()


#Main game loop
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()

    #Draw game here
    screen.fill(grass_color)
    fruit.draw_fruit()
    snake.draw_snake()

    pygame.display.update()
    clock.tick(60) #Limit the FPS to 60