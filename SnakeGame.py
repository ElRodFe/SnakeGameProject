import pygame
import sys
import random
from pygame.math import Vector2

#Create Snake class
class SNAKE:
     def __init__(self):
            self.body = [Vector2(5,10), Vector2(6,10), Vector2(7,10)]
            self.direction = Vector2(1,0)
            self.new_block = False

     def draw_snake(self):
          #Positioning each "piece" of the snake
          for block in self.body:
               x_pos = block.x*cell_size
               y_pos = block.y*cell_size
               snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
               pygame.draw.rect(screen, (102, 0, 0), snake_rect)
     
     def move_snake(self):
        if self.new_block == True:
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction) #insert the new "head" of the snake to the body
            self.body = body_copy[:]
            self.new_block = False
        else:
            body_copy = self.body[:-1] #take only two first vectors from the snake
            body_copy.insert(0,body_copy[0] + self.direction) #insert the new "head" of the snake to the body
            self.body = body_copy[:]
     
     def add_block(self):
          self.new_block = True

#Create fruit class
class FRUIT:
     def __init__(self):
          #Random position for fruit every time the game starts
          self.random_pos()
        
     def draw_fruit(self):
          fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
          pygame.draw.rect(screen, (255, 255, 51), fruit_rect)
     
     def random_pos(self):
          self.x = random.randint(0, cell_number - 1)
          self.y = random.randint(0, cell_number - 1)
          self.pos = Vector2(self.x, self.y)

class MAIN:
     def __init__(self):
          self.snake = SNAKE()
          self.fruit = FRUIT()
     
     def update(self):
          self.snake.move_snake()
          self.bite()
     
     def draw_elements(self):
        self.fruit.draw_fruit()
        self.snake.draw_snake()
     
     def bite(self):
          if self.fruit.pos == self.snake.body[0]: #Check if the snake's head touches the fruit
               self.fruit.random_pos() #make the fruit change its position when bitten
               self.snake.add_block() #make the snake bigger
    

pygame.init()

    ###Game program elements
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
grass_color = (51, 102, 0)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

#Main game loop
while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
         if event.type == SCREEN_UPDATE:
              main_game.update()
         if event.type == pygame.KEYDOWN: #Snake movement on keypress
              if event.key == pygame.K_UP:
                   main_game.snake.direction = Vector2(0,-1)
              if event.key == pygame.K_DOWN:
                   main_game.snake.direction = Vector2(0,1)
              if event.key == pygame.K_LEFT:
                   main_game.snake.direction = Vector2(-1,0)
              if event.key == pygame.K_RIGHT:
                   main_game.snake.direction = Vector2(1,0)

    #Draw game here
    screen.fill(grass_color)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) #Limit the FPS to 60