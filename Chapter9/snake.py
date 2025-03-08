import pygame
import sys
import random
import time

pygame.init()

window_x = 720
window_y = 480
green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
black = (0, 0, 0)

speed = 20

pygame.display.set_caption('Snake')
game = pygame.display.set_mode((window_x, window_y))
direction = 'RIGHT'
change_direction = direction

fps = pygame.time.Clock()

snake_position = [100, 50]
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]]
fruit_position = [random.randint(0, (window_x - 10) // 10) * 10, random.randint(0, (window_y-10) // 10) * 10]

score = 0
def show_score():
    score_font = pygame.font.SysFont('Arial', 20)
    score_surface = score_font.render('Score: ' + str(score), True, (255, 255, 255))
    score_rect = score_surface.get_rect()
    game.blit(score_surface, score_rect)

def game_over():
    game_over_font = pygame.font.SysFont("Arial", 50)
    game_over_surface = game_over_font.render('Game over, Your score is ' + str(score), True, (255, 182, 193))
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.center = (360, 240)
    game.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()


while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change_direction = 'UP'
            if event.key == pygame.K_DOWN:
                change_direction = 'DOWN'
            if event.key == pygame.K_LEFT:
                change_direction = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change_direction = 'RIGHT'

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if change_direction == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_direction == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if change_direction == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_direction == 'DOWN' and direction != 'UP':
        direction = 'DOWN'

    if direction == 'RIGHT':
        snake_position[0] = snake_position[0] + 10
    if direction == 'LEFT':
        snake_position[0] = snake_position[0] - 10
    if direction == 'UP':
        snake_position[1] = snake_position[1] - 10
    if direction == 'DOWN':
        snake_position[1] = snake_position[1] + 10


    snake_body.insert(0, list(snake_position))

    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score = score + 10
        fruit_position = [random.randint(0, (window_x - 10) // 10) * 10, random.randint(0, (window_y - 10) // 10) * 10]
    else:
        snake_body.pop()

    game.fill((138, 43, 226))

    if snake_position[0] > window_x or snake_position[1] > window_y:
        game_over()
    elif snake_position[0] < 0 or snake_position[1] < 0:
        game_over()

    for block in snake_body[1:]:
        if block[0] == snake_position[0] and block[1] == snake_position[1]:
            game_over()

    for position in snake_body:
        pygame.draw.rect(game, green, pygame.Rect(position[0], position[1], 10, 10))
    pygame.draw.rect(game, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    show_score()
    pygame.display.flip()
    fps.tick(speed)
