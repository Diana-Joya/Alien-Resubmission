import pygame
import pygame.font
from button import Button


class Start:
    def __init__(self, ai_settings, screen):
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.bg_color = (0, 0, 0)

        self.invader_one = InvaderOne()
        self.invader_two = InvaderTwo()
        self.invader_three = InvaderThree()
        self.invader_four = InvaderFour()

        self.play_button = "Play"
        self.play_y = 550
        self.scores_button = "High Scores"
        self.scores_y = 650

        self.prep_main_title()
        self.prep_alien_scores()

    def prep_main_title(self):
        self.title_high = "SPACE"
        self.title_high_color = (255, 255, 255)
        self.title_high_font = pygame.font.SysFont(None, 88)
        self.title_high_width, self.title_high_height = 80, 50
        self.title_high_rect = pygame.Rect(560, 80, self.title_high_width, self.title_high_height)
        self.title_high_image = self.title_high_font.render(self.title_high, True, self.title_high_color)
        self.title_high_image_rect = self.title_high_image.get_rect()
        self.title_high_image_rect.center = self.title_high_rect.center

        self.title_low = "INVADERS"
        self.title_low_color = (0, 255, 127)
        self.title_low_font = pygame.font.SysFont(None, 60)
        self.title_low_width, self.title_low_height = 80, 40
        self.title_low_rect = pygame.Rect(562, 124, self.title_low_width, self.title_low_height)
        self.title_low_image = self.title_low_font.render(self.title_low, True, self.title_low_color)
        self.title_low_image_rect = self.title_low_image.get_rect()
        self.title_low_image_rect.center = self.title_low_rect.center

    def prep_alien_scores(self):
        self.invader_one_alien = self.invader_one.invader_one
        self.invader_one_rect = self.invader_one.rect
        self.invader_one_image = self.invader_one.invader_one_image
        self.invader_one_image_rect = self.invader_one.invader_one_image_rect

        self.invader_two_alien = self.invader_two.invader_two
        self.invader_two_rect = self.invader_two.rect
        self.invader_two_image = self.invader_two.invader_two_image
        self.invader_two_image_rect = self.invader_two.invader_two_image_rect

        self.invader_three_alien = self.invader_three.invader_three
        self.invader_three_rect = self.invader_three.rect
        self.invader_three_image = self.invader_three.invader_three_image
        self.invader_three_image_rect = self.invader_three.invader_three_image_rect

        self.invader_four_alien = self.invader_four.invader_four
        self.invader_four_rect = self.invader_four.rect
        self.invader_four_image = self.invader_four.invader_four_image
        self.invader_four_image_rect = self.invader_four.invader_four_image_rect

    def render_play_button(self):
        self.play = Button(self.screen, self.play_button, self.play_y)
        self.play.draw_button()

    def render_score_button(self):
        self.scores = Button(self.screen, self.scores_button, self.scores_y)
        self.scores.draw_button()

    def draw_start_screen(self):
        self.screen.fill(self.bg_color, self.screen_rect)
        self.screen.blit(self.title_high_image, self.title_high_image_rect)
        self.screen.blit(self.title_low_image, self.title_low_image_rect)

        self.render_play_button()
        self.render_score_button()

        ''' Aliens '''
        self.screen.blit(self.invader_one_alien, self.invader_one_rect)
        self.screen.blit(self.invader_one_image, self.invader_one_image_rect)
        self.screen.blit(self.invader_two_alien, self.invader_two_rect)
        self.screen.blit(self.invader_two_image, self.invader_two_image_rect)
        self.screen.blit(self.invader_three_alien, self.invader_three_rect)
        self.screen.blit(self.invader_three_image, self.invader_three_image_rect)
        self.screen.blit(self.invader_four_alien, self.invader_four_rect)
        self.screen.blit(self.invader_four_image, self.invader_four_image_rect)


class InvaderOne:
    def __init__(self):
        self.invader_one = pygame.image.load('images/mellow.png')
        self.rect = self.invader_one.get_rect()
        self.rect.centerx = 532
        self.rect.centery = 220
        self.invader_one_score = "= 10 PTS"
        self.invader_one_score_color = (255, 255, 255)
        self.invader_one_font = pygame.font.SysFont(None, 35)
        self.invader_one_image = self.invader_one_font.render(self.invader_one_score, True,
                                                              self.invader_one_score_color)
        self.invader_one_image_rect = pygame.Rect(613, 210, 50, 50)


class InvaderTwo:
    def __init__(self):
        self.invader_two = pygame.image.load('images/mid.png')
        self.rect = self.invader_two.get_rect()
        self.rect.centerx = 532
        self.rect.centery = 275
        self.invader_two_score = "= 20 PTS"
        self.invader_two_score_color = (255, 255, 255)
        self.invader_two_font = pygame.font.SysFont(None, 35)
        self.invader_two_image = self.invader_two_font.render(self.invader_two_score, True,
                                                              self.invader_two_score_color)
        self.invader_two_image_rect = pygame.Rect(613, 262, 50, 50)


class InvaderThree:
    def __init__(self):
        self.invader_three = pygame.image.load('images/Boss.png')
        self.rect = self.invader_three.get_rect()
        self.rect.centerx = 532
        self.rect.centery = 335
        self.invader_three_score = "= 40 PTS"
        self.invader_three_score_color = (255, 255, 255)
        self.invader_three_font = pygame.font.SysFont(None, 35)
        self.invader_three_image = self.invader_three_font.render(self.invader_three_score, True,
                                                                  self.invader_three_score_color)
        self.invader_three_image_rect = pygame.Rect(613, 325, 50, 50)


class InvaderFour:
    def __init__(self):
        self.invader_four = pygame.image.load('images/UFO/invader 4.png')
        self.rect = self.invader_four.get_rect()
        self.rect.centerx = 532
        self.rect.centery = 405
        self.invader_four_score = "=  ???"
        self.invader_four_score_color = (255, 255, 255)
        self.invader_four_font = pygame.font.SysFont(None, 35)
        self.invader_four_image = self.invader_four_font.render(self.invader_four_score, True,
                                                                self.invader_four_score_color)
        self.invader_four_image_rect = pygame.Rect(613, 395, 50, 50)
