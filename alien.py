import pygame
import os
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, ai_settings, screen, color):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.my_points = 0
        self.images = self.init_alien(color)

        self.index = 0
        self.image = self.images[self.index]

        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.height = self.rect
        self.x = float(self.rect.x)

        self.prep_explosion()

    def init_alien(self, color):
        images = []
        path = 'images/Greenie/'
        if color == "green":
            path = 'images/Greenie/'
            self.my_points = 10
        elif color == "yellow":
            path = 'images/Yellow Mellow/'
            self.my_points = 10
        elif color == "purple":
            path = 'images/Purple/'
            self.my_points = 10
        elif color == "blue":
            path = 'images/Blue/'
            self.my_points = 10
        elif color == "green_boss":
            path = 'images/Green/'
            self.my_points = 40
        elif color == "aqua":
            path = 'images/Aqua/'
            self.my_points = 20

        for file_name in os.listdir(path):
            alien = pygame.image.load(path + os.sep + file_name)
            images.append(alien)
        return images

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def prep_explosion(self):
        self.explosion = []
        self.prev_y = self.rect.bottom
        self.prev_x = self.rect.centerx
        self.exp_index = 0

        path = 'images/alien explosion/'
        for file_name in os.listdir(path):
            alien = pygame.image.load(path + os.sep + file_name)
            self.explosion.append(alien)

    def alien_explosion(self):
        self.image = self.explosion[self.exp_index]
        self.rect = self.image.get_rect()
        self.rect.centerx = self.prev_x
        self.rect.bottom = self.prev_y

    def update_explosion(self):
        if self.exp_index < len(self.images):
            self.alien_explosion()
            self.exp_index += 1
        elif self.exp_index >= len(self.images):
            self.ai_settings.alien_explosion = False

    def update(self):
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
