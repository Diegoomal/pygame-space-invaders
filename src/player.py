import pygame
import config

from bullet import Bullet

class Player:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.bullets = []

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def move(self, direction):
        self.x += direction * self.speed
        if self.x < 0:
            self.x = 0
        elif self.x > config.SCREEN_WIDTH - self.width:
            self.x = config.SCREEN_WIDTH - self.width

    def shoot(self):
        bullet = Bullet(self.x + self.width // 2, self.y, 5, 10, -10, config.WHITE)
        self.bullets.append(bullet)

    def update_bullets(self, screen):
        for bullet in self.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                self.bullets.remove(bullet)
            else:
                bullet.draw(screen)


