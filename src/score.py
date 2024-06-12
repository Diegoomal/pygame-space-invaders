import pygame
import config

class Score:

    def __init__(self, screen, margin, color):
        self.screen = screen
        self.margin = margin
        self.color = color

    def draw(self, score):
        font = pygame.font.SysFont(None, config.FONT_SIZE)
        text = font.render(f"Score: {score}", True, self.color)
        self.screen.blit(text, [self.margin+5, self.margin+5])