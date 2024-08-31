import pygame
import sys
import random

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
fruit_position = [random.randint(0, window_x), random.randint(0, window_y)]

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
    snake_body.pop(4)

    game.fill(black)

    for position in snake_body:
        pygame.draw.rect(game, green, pygame.Rect(position[0], position[1], 10, 10))
    pygame.draw.rect(game, red, pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))

    pygame.display.flip()
    fps.tick(speed)
