import pygame
import config

class GameEnvironment:
    def __init__(self, screen, margin, color):
        self.screen = screen
        self.margin = margin
        self.color = color

    def draw(self):
        pygame.draw.rect(self.screen, self.color, [self.margin, self.margin, config.SCREEN_WIDTH - 2 * self.margin, config.SCREEN_HEIGHT - 2 * self.margin], 2)
