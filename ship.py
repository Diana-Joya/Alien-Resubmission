import pygame
import os
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False

        self.prep_explosion()

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def prep_explosion(self):
        self.images = []
        path = 'images/Ship explosion/'
        for file_name in os.listdir(path):
            explosion = pygame.image.load(path + os.sep + file_name)
            self.images.append(explosion)
        self.index = 0

    def explosion(self):
        prev_y = self.rect.bottom
        prev_x = self.rect.centerx
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.centerx = prev_x
        self.rect.bottom = prev_y

    def update_explosion(self):
        if self.index < len(self.images):
            self.explosion()
            self.index += 1
        elif self.index > len(self.images):
            self.ai_settings.explode = False

    def restore_image(self):
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)
        self.index = 0
