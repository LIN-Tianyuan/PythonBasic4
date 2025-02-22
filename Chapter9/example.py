import pygame

from Chapter9.snake import snake_position

fps = pygame.time.Clock()

speed = 20

pygame.draw.rect(game, (255, 255, 255), pygame.Rect(fruit_position[0], fruit_position[1], 10, 10))
pygame.draw.rect(game, (0, 255, 0), pygame.Rect(snake_body[0][0], snake_body[0][1], 10, 10))
# pygame.draw.rect(game, (0, 255, 0), pygame.Rect(snake_position[0], snake_position[1], 10, 10))

direction = 'RIGHT'
change_direction = direction
while True:
    for event in pygame.event.get():
        # Gestion des événements clés
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                change_direction = 'RIGHT'
            if event.key == pygame.K_LEFT:
                change_direction = 'LEFT'
            if event.key == pygame.K_UP:
                change_direction = 'UP'
            if event.key == pygame.K_DOWN:
                change_direction = 'DOWN'
        if change_direction == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_direction == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_direction == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_direction == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'RIGHT':
            snake_position[0] = snake_position[0] + 10
        if direction == 'LEFT':
            snake_position[0] = snake_position[0] - 10
        if direction == 'UP':
            snake_position[1] = snake_position[1] - 10
        if direction == 'DOWN':
            snake_position[1] = snake_position[1] + 10


        [110, 50],
        [100, 50],
        [90, 50],
        [80, 50],
        [70, 50]

        snake_body.insert(0, list(snake_position))
        snake_body.pop(4)
        game.fill()
        fps.tick(speed)






        if event.type == pygame.QUIT:
            pygame.quit()


