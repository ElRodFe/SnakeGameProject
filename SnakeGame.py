import pygame
import sys
import random
from pygame.math import Vector2

#Create Snake class
class SNAKE:
     def __init__(self):
            self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)]
            self.direction = Vector2(0,0) #snake static until you press a key
            self.new_block = False
            self.bite_sound = pygame.mixer.Sound("sounds/bite.mp3")

     def draw_snake(self):
          #Positioning each "piece" of the snake
          for block in self.body:
               x_pos = block.x*cell_size
               y_pos = block.y*cell_size
               snake_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)
               pygame.draw.rect(screen, (64, 64, 64), snake_rect)
     
     def move_snake(self):
        if self.new_block == True:  #make the snake grow when eating the fruit
            body_copy = self.body[:]
            body_copy.insert(0,body_copy[0] + self.direction) 
            self.body = body_copy[:]
            self.new_block = False #set to false again to prevent the snake to grow infinitely
        else:  #move the snake normally
            body_copy = self.body[:-1] #take only two first vectors from the snake
            body_copy.insert(0,body_copy[0] + self.direction) #insert the new "head" of the snake to the body
            self.body = body_copy[:]
     
     def add_block(self):
          self.new_block = True

     def play_bite_sound(self):
          self.bite_sound.play()

     def reset(self):
          self.body = [Vector2(5,10), Vector2(4,10), Vector2(3,10)] #reset the snake
          self.direction = Vector2(0,0) #snake static until you press a key

#Create fruit class
class FRUIT:
     def __init__(self):
          #Random position for fruit every time the game starts
          self.random_pos()
        
     def draw_fruit(self):
          fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
          screen.blit(apple, fruit_rect)
          #pygame.draw.rect(screen, (204, 0, 0), fruit_rect)
     
     def random_pos(self):
          self.x = random.randint(0, cell_number - 1)
          self.y = random.randint(0, cell_number - 1)
          self.pos = Vector2(self.x, self.y)

#Game Logic 
class MAIN:
     def __init__(self):
          self.snake = SNAKE()
          self.fruit = FRUIT()
     
     def update(self):
          self.snake.move_snake()
          self.bite()
          self.check_fail()
     
     def draw_elements(self):
        self.draw_grass()
        self.fruit.draw_fruit()
        self.snake.draw_snake()
        self.draw_score()
     
     def bite(self):
          if self.fruit.pos == self.snake.body[0]: #Check if the snake's head touches the fruit
               self.fruit.random_pos() #make the fruit change its position when bitten
               self.snake.add_block() #make the snake bigger
               self.snake.play_bite_sound()

          for block in self.snake.body[0:]: #Avoid the fruit from spawning on the snake's body
               if block == self.fruit.pos:
                    self.fruit.random_pos()

     def check_fail(self):
          #check if the snake hits the border of the screen
          if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
               self.game_over()

          #check if the snake hits itself
          for block in self.snake.body[1:]:
               if block == self.snake.body[0]:
                    self.game_over()

     def game_over(self):
          self.snake.reset()
     
     def draw_grass(self):
          grass_color = (51, 95, 0)
          for row in range(cell_number):
               if row % 2 == 0:
                    for col in range(cell_number):
                         if col % 2 == 0:
                              grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                              pygame.draw.rect(screen, grass_color, grass_rect)
               else:
                    for col in range(cell_number):
                         if col % 2 != 0:
                              grass_rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
                              pygame.draw.rect(screen, grass_color, grass_rect)

     def draw_score(self):
          score_text = str(len(self.snake.body) - 3) #Get the score given the length of the snake
          score_surface = game_font.render(score_text, True, (0,0,0))

          #Creante positioning for the score in screen and insert it
          score_x = int(cell_size * cell_number - 60)
          score_y = int(cell_size * cell_number - 40)
          score_rect = score_surface.get_rect(center = (score_x, score_y))
          screen.blit(score_surface, score_rect)

pygame.mixer.pre_init(44100, -16, 512)
pygame.init()

    ###Game program elements
cell_size = 40
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()
grass_color = (51, 102, 0)
game_font = pygame.font.Font(None, 25) #Default fonr from PyGame for text

apple = pygame.image.load("graphics/apple.png").convert_alpha() #import the fruit image
apple = pygame.transform.scale(apple, (cell_size, cell_size)) #make the image the size of a block


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
                   if main_game.snake.direction.y != 1:
                         main_game.snake.direction = Vector2(0,-1)
              if event.key == pygame.K_DOWN:
                   if main_game.snake.direction.y != -1:
                         main_game.snake.direction = Vector2(0,1)
              if event.key == pygame.K_LEFT:
                   if main_game.snake.direction.x != 1:
                         main_game.snake.direction = Vector2(-1,0)
              if event.key == pygame.K_RIGHT:
                   if main_game.snake.direction.x != -1:
                         main_game.snake.direction = Vector2(1,0)

    #Draw game here
    screen.fill(grass_color)
    main_game.draw_elements()
    pygame.display.update()
    clock.tick(60) #Limit the FPS to 60