import sys
import pygame

from time import sleep
from bullet_animations import BulletAnimation
from alien_animations import AlienAnimations


class Update:
    def __init__(self, ai_settings, screen, ship, bullets, aliens, stats, sb, start_screen, score_board,
                 random_ufo, bunkers):
        self.screen = screen
        self.ai_settings = ai_settings
        self.ship = ship
        self.bullets = bullets
        self.bunkers = bunkers
        self.aliens = aliens
        self.random_ufo = random_ufo
        self.stats = stats
        self.sb = sb
        self.start_screen = start_screen
        self.score_board = score_board
        self.bullet_animation = BulletAnimation(ai_settings, screen, ship, bullets, aliens, stats, sb,
                                                random_ufo, bunkers)
        self.alien_animation = AlienAnimations(ai_settings, screen, ship, aliens)

    def update_screen(self):
        self.screen.fill(self.ai_settings.bg_color)

        ''' Sprites '''
        for self.bullet in self.bullets.sprites():
            self.bullet.draw_bullet()
        self.animate_explosion()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.bunkers.draw(self.screen)
        self.random_ufo.blitme()

        ''' Scoreboard '''
        self.sb.show_score()

        if not self.stats.game_active:
            self.start_screen.draw_start_screen()
        if self.stats.sb_active:
            self.score_board.draw_scoreboard_screen()

        ''' Make most recently drawn screen visible '''
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            self.event = event
            if self.event.type == pygame.QUIT:
                sys.exit()
            elif self.event.type == pygame.KEYDOWN:
                self.check_keydown_events()
            elif self.event.type == pygame.KEYUP:
                self.check_keyup_events()
            elif self.event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
                self.check_button()

    def check_keydown_events(self):
        if self.event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif self.event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif self.event.key == pygame.K_SPACE:
            self.bullet_animation.fire_bullet()
        elif self.event.key == pygame.K_q or self.event.key == pygame.K_ESCAPE:
            sys.exit()

    def check_keyup_events(self):
        if self.event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif self.event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def check_button(self):
        play_button = self.start_screen.play.rect.collidepoint(self.mouse_x, self.mouse_y)
        scores_button = self.start_screen.scores.rect.collidepoint(self.mouse_x, self.mouse_y)
        if play_button:
            self.check_play_button()
        elif scores_button:
            self.check_score_button()

    def check_score_button(self):
        self.stats.sb_active = True

    def check_play_button(self):
        if not self.stats.game_active:
            ''' Start Game '''
            self.ai_settings.initialize_dynamic_settings()

            pygame.mouse.set_visible(False)

            self.stats.reset_stats()
            self.stats.game_active = True

            self.sb.prep_score()
            self.sb.prep_high_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()
            self.bunkers.empty()

            self.bullet_animation.set_protection()
            self.alien_animation.create_fleet_low()
            self.alien_animation.create_fleet_medium()
            self.alien_animation.create_fleet_high()
            self.ship.center_ship()

    def ship_hit(self):
        if self.stats.ships_left > 0:
            ''' Decrement Lives '''
            self.stats.ships_left -= 1
            self.ai_settings.explode = False

            ''' Update Scoreboard & Reset Level '''
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self.bunkers.empty()
            self.bullet_animation.set_protection()
            self.alien_animation.create_fleet_low()
            self.alien_animation.create_fleet_medium()
            self.alien_animation.create_fleet_high()
            self.ship.center_ship()
            self.random_ufo.resetme()

            sleep(0.3)

        else:
            self.stats.game_over = True
            self.stats.check_end_score = 1
            self.sb.check_high_score()
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

    def animate_explosion(self):
        explode = pygame.mixer.Sound('music/explosion.wav')
        if self.ai_settings.explode and self.ship.index == len(self.ship.images):
            self.ship.index = 0
            self.ship.restore_image()
            self.ship_hit()
            self.ai_settings.explode = False
            pygame.mixer.Sound.play(explode)
        if self.ai_settings.explode:
            self.ship.update_explosion()

        if self.ai_settings.ufo_explode:
            self.random_ufo.show_score()
        if self.ai_settings.ufo_explode and self.random_ufo.ready:
            self.random_ufo.resetme()
            self.ai_settings.ufo_explode = False
            self.random_ufo.ready = False
