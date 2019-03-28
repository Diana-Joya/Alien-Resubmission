import pygame

from events import Update
from alien_animations import AlienAnimations


class Collisions:
    def __init__(self, ai_settings, screen, ship, bullets, aliens, stats, sb, start_screen, score_board, random_ufo,
                 bunkers):
        self.ai_settings = ai_settings
        self.screen = screen
        self.ship = ship
        self.bullets = bullets
        self.aliens = aliens
        self.stats = stats
        self.sb = sb
        self.start_screen = start_screen
        self.event = Update(ai_settings, screen, ship, bullets, aliens, stats, sb, start_screen, score_board,
                            random_ufo, bunkers)
        self.alien_animation = AlienAnimations(ai_settings, screen, ship, aliens)
        self.bunkers = bunkers

    def check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break

    def change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.ai_settings.fleet_drop_speed
        self.ai_settings.fleet_direction *= -1

    def check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self.ai_settings.explode = True
                break

    def update_aliens(self):
        self.check_fleet_edges()
        self.aliens.update()

        ''' Alien-Ship Collisions '''
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ai_settings.explode = True

        ''' Aliens Reach Bottom of Screen '''
        self.check_aliens_bottom()
