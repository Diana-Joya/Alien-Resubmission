import pygame
from pygame.sprite import Sprite


class Bunker(Sprite):
    def __init__(self, ai_settings, screen, color):
        super(Bunker, self).__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        self.height = 30
        self.width = 80
        self.color = color

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.y = 560

    def update(self):
        self.screen.blit(self.image, self.rect)
