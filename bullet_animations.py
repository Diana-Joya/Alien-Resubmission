import pygame

from bullet import Bullet
from alien_animations import AlienAnimations
from alien import Alien
from bunkers import Bunker


class BulletAnimation:
    def __init__(self, ai_settings, screen, ship, bullets, aliens, stats, sb, random_ufo, bunkers):
        self.ai_settings = ai_settings
        self.screen = screen
        self.ship = ship
        self.bullets = bullets
        self.alien_bullets = bullets
        self.aliens = aliens
        self.stats = stats
        self.sb = sb
        self.ufo = random_ufo
        self.bunkers = bunkers
        self.al = Alien(ai_settings, screen, "green")
        self.alien_animations = AlienAnimations(ai_settings, screen, ship, aliens)

    def fire_bullet(self):
        if len(self.bullets) < self.ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings=self.ai_settings, screen=self.screen,
                                ship=self.ship, yoffset=self.ship.rect.height)
            self.bullets.add(new_bullet)
            shoot = pygame.mixer.Sound('music/shoot.wav')
            pygame.mixer.Sound.play(shoot)
        self.bullets.update()

    def fire_alien_bullet(self):
        if len(self.alien_bullets) < self.ai_settings.alien_bullets_allowed:
            new_bullet = Bullet(ai_settings=self.ai_settings, screen=self.screen,
                                ship=self.ship, yoffset=self.screen.y + self.al.height)
            self.alien_bullets.add(new_bullet)
        self.alien_bullets.update_alien_b()

    def update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()
        self.check_bunker_collisions()

    def update_alien_bullets(self):
        self.alien_bullets.update_alien_b()

        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self.check_bullet_alien_collisions()
        self.check_bunker_collisions()

    def check_bunker_collisions(self):
        pygame.sprite.groupcollide(self.bullets, self.bunkers, True, True)
        for alien in self.aliens.copy():
            if alien.rect.bottom >= 560:
                pygame.sprite.groupcollide(self.aliens, self.bunkers, False, True)

    def check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(self.aliens, self.bullets, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.ai_settings.alien_score
                self.sb.prep_score()
            self.sb.check_high_score()

        if len(self.aliens) == 0:
            self.bullets.empty()
            self.ai_settings.increase_speed()

            self.stats.level += 1
            self.sb.prep_level()

            self.set_protection()
            self.alien_animations.create_fleet_low()
            self.alien_animations.create_fleet_medium()
            self.alien_animations.create_fleet_high()

        ufo_collisions = pygame.sprite.spritecollide(self.ufo, self.bullets, True)
        if ufo_collisions:
            self.ufo.prep_score()
            self.stats.score += self.ufo.score
            self.sb.prep_score()
            self.sb.check_high_score()
            self.ai_settings.ufo_explode = True

    def set_protection(self):
        update_color = 0
        for bunker in range(4):
            if update_color == 0:
                color = (150, 238, 238)
            elif update_color == 1:
                color = (32, 178, 170)
            elif update_color == 2:
                color = (0, 206, 209)
            else:
                color = (135, 206, 250)
            for column in range(4):
                self.bunker = Bunker(self.ai_settings, self.screen, color)
                self.bunker.rect.x = 200 + (self.bunker.width * bunker) + (2 * self.bunker.width * bunker)
                self.bunkers.add(self.bunker)
            update_color += 1
