import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Snake and fruit initialization
snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)
fruit = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
         random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
score = 0
WIN_CONDITION = 10

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_fruit(fruit):
    pygame.draw.rect(screen, RED, (*fruit, CELL_SIZE, CELL_SIZE))

def move_snake(snake, direction):
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    return [new_head] + snake[:-1]

def check_collision(snake):
    head = snake[0]
    # Check wall collision
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        return True
    # Check self collision
    if head in snake[1:]:
        return True
    return False

def spawn_fruit(snake):
    while True:
        new_fruit = (random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
                     random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE)
        if new_fruit not in snake:
            return new_fruit

# Game loop
running = True
while running:
    screen.fill(BLACK)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, CELL_SIZE):
                snake_dir = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -CELL_SIZE):
                snake_dir = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and snake_dir != (CELL_SIZE, 0):
                snake_dir = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-CELL_SIZE, 0):
                snake_dir = (CELL_SIZE, 0)

    # Move snake
    snake = move_snake(snake, snake_dir)

    # Check for collisions
    if check_collision(snake):
        print("Game Over! You hit something.")
        running = False

    # Check if snake eats fruit
    if snake[0] == fruit:
        score += 1
        snake.append(snake[-1])  # Grow snake
        fruit = spawn_fruit(snake)

    # Check win condition
    if score == WIN_CONDITION:
        print("You Win!")
        running = False

    # Draw everything
    draw_snake(snake)
    draw_fruit(fruit)
    pygame.display.flip()

    # Control frame rate
    clock.tick(10)

pygame.quit()
sys.exit()