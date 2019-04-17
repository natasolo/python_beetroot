""""
    Conditions of game:
    If the snake eats an apple, the apple moves to a new position.
    If the snake eats an apple, the snakes length grows.
    If a snake collapses with itself or boundaries, game over.
"""
import pygame
import random
import time
pygame.init()


class Play():
    def __init__(self):
        self.screen_width = 500
        self.screen_height = 500
        self.speed = 1
        self.score = 0
        self.fsp_control = pygame.time.Clock() #frame per second controller
        self.black = pygame.Color(0, 0, 0)
        self.white = pygame.Color(255, 255, 255)
        self.green = pygame.Color(0, 255, 0)
        self.red = pygame.Color(255, 0, 0)


    def surface_and_title_of_game(self):
        self.play_surface = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('My_Snake_Game')


    def event_loop(self, change_to): #to track player keystrokes
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                elif event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                elif event.key == pygame.K_UP:
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
        return change_to


    def refresh_screen_and_fsp(self):
        pygame.display.flip()
        game.fsp_control.tick(23)


    def show_score(self, choice=1):
        my_font = pygame.font.SysFont('vernada', 35, 'bold')
        my_surf = my_font.render('Score: {0}'.format(self.score), True, self.black)
        my_rect = my_surf.get_rect()
        if choice == 1:
            my_rect.midtop = (90, 15)
        self.play_surface.blit(my_surf, my_rect)

    def game_over(self):
        move_font = pygame.font.SysFont('vernada', 70, 'bold')
        move_surf = move_font.render('Game over', True, self.black)
        move_rect = move_surf.get_rect()
        move_rect.midtop = (360, 15)
        self.play_surface.blit(move_surf, move_rect)
        self.show_score(0)
        pygame.display.flip()
        time.sleep(10)
        pygame.quit()


class Snake():
    def __init__(self, snake_color):
        self.snake_head_pos = [100, 50]  # [x, y], position of snake's head
        self.snake_body = [[100, 50], [90, 50], [80, 50]]  # position of snake's body,
                                                            # the first element -> head, the last -> tail
        self.snake_color = snake_color
        self.direction = "RIGHT" # intial direction of the snake
        self.change_to = self.direction # change direction of the snake

    def change_position_of_head(self):
        if self.direction == "RIGHT":
            self.snake_head_pos[0] += 10
        elif self.direction == "LEFT":
            self.snake_head_pos[0] -= 10
        elif self.direction == "UP":
            self.snake_head_pos[1] -= 10
        elif self.direction == "DOWN":
            self.snake_head_pos[1] += 10

    def change_direction(self):
        if self.change_to == "RIGHT" and not self.direction == "LEFT":
            self.direction = self.change_to
        elif self.change_to== "LEFT" and not self.direction == "RIGHT":
            self.direction = self.change_to
        elif self.change_to == "UP" and not self.direction == "DOWN":
            self.direction = self.change_to
        elif self.change_to == "DOWN" and not self.direction == "UP":
            self.direction = self.change_to

    def snake_eats_apple_and_score(self, score, apple_position, screen_width, screen_height):
        self.snake_body.insert(0, list(self.snake_head_pos))
        if self.snake_head_pos[0] == apple_position[0]:
            if self.snake_head_pos[1] == apple_position[1]:
                    apple_position = [random.randrange(1, screen_width / 10) * 10, # if the snake eats an apple, the apple goes to a new random position
                    random.randrange(1, screen_height / 10) * 10]
                    score += 1 # increase score by one
        else:
            self.snake_body.pop()
        return score, apple_position

    def check_for_collisions(self, game_over, screen_width, screen_height):
        if self.snake_head_pos[0] > screen_width-10 or self.snake_head_pos[0] < 0: #collision with boundaries
            game_over()
        if self.snake_head_pos[1] > screen_height-10 or self.snake_head_pos[1] < 0: #collision with boundaries
            game_over()
        for item in self.snake_body[1:]: #collision with itself
            if item[0] == self.snake_head_pos[0] and item[1] == self.snake_head_pos[1]:
                    game_over()

    def draw_snake(self, play_surface, surface_color):
        play_surface.fill(surface_color)
        for position in self.snake_body:
            pygame.draw.rect(
                play_surface, self.snake_color, pygame.Rect(
                    position[0], position[1], 10, 10)) # rect() has 3 arguments: surface, color and object, =>x,y, size x , size y).


class Apple():
    def __init__(self, apple_color, screen_width, screen_height):
        self.apple_color = apple_color
        self.apple_size_x = 10
        self.apple_size_y = 10
        self.apple_position = [random.randrange(1, screen_width/10)*10, # random placement of new apple
                              random.randrange(1, screen_height/10)*10]

    def draw_apple(self, play_surface):
        pygame.draw.rect(
            play_surface, self.apple_color, pygame.Rect(
                self.apple_position[0], self.apple_position[1],
                self.apple_size_x, self.apple_size_y)) # rect() has 3 arguments: surface, color and object, =>x,y, size x , size y).


game = Play()
snake = Snake(game.red)
apple = Apple(game.green, game.screen_width, game.screen_height)


game.surface_and_title_of_game()

while True:
    snake.change_to = game.event_loop(snake.change_to)

    snake.change_direction()
    snake.change_position_of_head()
    game.score, apple.apple_position = snake.snake_eats_apple_and_score(game.score, apple.apple_position, game.screen_width, game.screen_height)
    snake.draw_snake(game.play_surface, game.white)

    apple.draw_apple(game.play_surface)

    snake.check_for_collisions(game.game_over, game.screen_width, game.screen_height)

    game.show_score()
    game.refresh_screen_and_fsp()
