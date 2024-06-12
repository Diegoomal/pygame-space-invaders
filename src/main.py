import pygame
import config
from player import Player, Bullet
from enemy import Enemy
from environment import GameEnvironment
from score import Score
from game_funcs import detect_collision

# Initialize Pygame
pygame.init()

# Config screen
pygame.display.set_caption(config.GAME_TITLE)
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

# Create Player, Enemy e GameEnvironment
score = Score(screen, 10, config.WHITE)
player = Player(config.SCREEN_WIDTH // 2 - 25, config.SCREEN_HEIGHT - 70, 50, 50, 10, config.GREEN)
enemies = [Enemy(x * 60, 50, 40, 40, 5, config.RED) for x in range(10)]
environment = GameEnvironment(screen, 10, config.WHITE)

# Player score
score_value = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.move(-1)
            elif event.key == pygame.K_RIGHT:
                player.move(1)
            elif event.key == pygame.K_SPACE:
                player.shoot()

    # Movimento dos inimigos
    [enemy.move(config.SCREEN_WIDTH) for enemy in enemies]

    # Verify collision    
    score_value = detect_collision(player, enemies, score_value)    

    # Draw screen
    screen.fill(config.BLACK)
    environment.draw()
    player.draw(screen)
    player.update_bullets(screen)
    [enemy.draw(screen) for enemy in enemies]
    score.draw(score_value)

    pygame.display.flip()
    pygame.time.Clock().tick(config.CLOCKS)

pygame.quit()
