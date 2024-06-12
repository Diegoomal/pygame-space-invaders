import pygame

class Enemy:
    def __init__(self, x, y, width, height, speed, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.color = color
        self.direction = 1

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, [self.x, self.y, self.width, self.height])

    def move(self, screen_width):
        self.x += self.speed * self.direction
        if self.x <= 0 or self.x >= screen_width - self.width:
            self.direction *= -1
            self.y += self.height
