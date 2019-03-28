import pygame
import random
import math
from pygame.sprite import Sprite


class UFO(Sprite):
    def __init__(self, ai_settings, screen):
        super(UFO, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/UFO/invader 4.png')

        self.rect = self.image.get_rect(topleft=(-200, 35))
        self.direction = 1
        self.move_time = 1000
        self.timer = pygame.time.get_ticks()
        self.random_interval()
        self.ufo_score()
        self.ready = False

        self.ufo_music = 'music/random_ufo.wav'
        self.loop = 0

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self, current_time):
        reset = False
        time_passed = current_time - self.timer
        if time_passed > self.move_time:
            if (self.rect.x > 50) and (self.rect.x < 1150):
                pygame.mixer.music.load(self.ufo_music)
                pygame.mixer.music.play(self.loop)
            else:
                pygame.mixer.music.stop()
            if (self.rect.x < 1950 or self.rect.x > 5000) and self.direction == 1:
                self.rect.x += self.ai_settings.ufo_speed_factor
                self.blitme()
            if self.rect.x > -1200 and self.direction == -1:
                self.rect.x -= self.ai_settings.ufo_speed_factor
                self.blitme()

        if self.rect.x > 5350:
            self.ready = True

        if self.rect.x > 1940 and not self.rect.x > 5000:
            self.direction = -1
            reset = True
        if self.rect.x < -1190:
            self.direction = 1
            reset = True
        if time_passed > self.move_time and reset and self.ready:
            self.timer = current_time
            self.random_interval()

    def resetme(self):
        self.direction = int(random.choice([-1, 1]))
        if self.direction == -1:
            self.rect.x = 1250
        if self.direction == 1:
            self.rect.x = -150

    def random_interval(self):
        if self.direction == -1:
            self.rect.x = random.randrange(1300, 1900)
        if self.direction == 1:
            self.rect.x = random.randrange(-1200, -180)

    def ufo_get_score(self):
        score = random.randrange(50, 500)
        return score

    def ufo_score(self):
        self.score = math.floor(self.ufo_get_score())
        self.text_color = (132, 112, 255)
        self.font = pygame.font.SysFont(None, 39)

    def prep_score(self):
        self.prev_y = self.rect.bottom
        self.prev_x = self.rect.centerx
        self.ufo_score()
        self.score_image = self.font.render(str(self.score), True, self.text_color,
                                            self.ai_settings.bg_color)
        self.score_rect = self.image.get_rect()
        self.rect.x = 5050
        self.direction = 1

    def show_score(self):
        self.score_rect.centerx = self.prev_x
        self.score_rect.bottom = self.prev_y
        self.screen.blit(self.score_image, self.score_rect)
