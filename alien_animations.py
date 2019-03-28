from alien import Alien
import random


class AlienAnimations:
    def __init__(self, ai_settings, screen, ship, aliens):
        self.ai_settings = ai_settings
        self.screen = screen
        self.aliens = aliens
        self.ship = ship
        self.my_alien = 0

    def create_alien(self, alien_number, row_number, color, points):
        self.alien = Alien(self.ai_settings, self.screen, color)
        self.alien_width = self.alien.rect.width
        self.alien.x = self.alien_width + 1.5 * self.alien_width * alien_number
        self.alien.rect.x = self.alien.x
        self.alien.my_points = points
        pos = self.get_alien_pos()
        self.alien.rect.y = (self.alien.rect.height + 1 * self.alien.rect.height * row_number) + \
                            (self.alien.rect.height * pos)
        self.aliens.add(self.alien)

    def create_fleet_low(self):
        self.my_alien = random.randrange(0, 4)
        current = self.get_alien_type()
        self.alien = Alien(self.ai_settings, self.screen, current)
        self.number_aliens_x = self.get_number_aliens_x()
        self.number_rows = self.rows_low_alien()
        self.alien_points = 10

        for row_number in range(self.number_rows):
            for alien_number in range(self.number_aliens_x):
                current = self.get_alien_type()
                self.create_alien(alien_number, row_number, current, self.alien_points)
                self.my_alien = random.randrange(0, 4)

    def create_fleet_medium(self):
        self.my_alien = 5
        current = self.get_alien_type()
        self.alien = Alien(self.ai_settings, self.screen, current)
        self.number_aliens_x = self.get_number_aliens_x()
        self.number_rows = self.rows_mid_alien()
        self.alien_points = 20

        for row_number in range(self.number_rows):
            for alien_number in range(self.number_aliens_x):
                self.create_alien(alien_number, row_number, current, self.alien_points)

    def create_fleet_high(self):
        self.my_alien = 4
        current = self.get_alien_type()
        self.alien = Alien(self.ai_settings, self.screen, current)
        self.number_aliens_x = self.get_number_aliens_x()
        self.number_rows = self.rows_hi_alien()
        self.alien_points = 40

        for row_number in range(self.number_rows):
            for alien_number in range(self.number_aliens_x):
                self.create_alien(alien_number, row_number, current, self.alien_points)

    def get_alien_type(self):
        if self.my_alien == 0:
            return "green"
        elif self.my_alien == 1:
            return "yellow"
        elif self.my_alien == 2:
            return "purple"
        elif self.my_alien == 3:
            return "blue"
        elif self.my_alien == 4:
            return "green_boss"
        elif self.my_alien == 5:
            return "aqua"

    def get_number_aliens_x(self):
        available_space_x = self.ai_settings.screen_width - 1.5 * self.alien.rect.width
        number_aliens_x = int(available_space_x / (1.4 * self.alien.rect.width))
        return number_aliens_x

    def rows_low_alien(self):
        #self.available_space_y = (self.ai_settings.screen_height - (3 * self.alien.rect.height) - self.ship.rect.height)
        #number_rows = int(self.available_space_y / (2 * self.alien.rect.height))
        number_rows = 2
        return number_rows

    def rows_mid_alien(self):
        self.available_space_y = (self.ai_settings.screen_height - (3 * self.alien.rect.height) - self.ship.rect.height)
        number_rows = int(self.available_space_y / (2 * self.alien.rect.height))
        return number_rows

    def rows_hi_alien(self):
        self.available_space_y = (self.ai_settings.screen_height - (3 * self.alien.rect.height) - self.ship.rect.height)
        number_rows = int(self.available_space_y / (2 * self.alien.rect.height))
        return number_rows

    def get_alien_pos(self):
        pos = 0
        if self.my_alien == 0 or self.my_alien == 1 or self.my_alien == 2 or self.my_alien == 3:
            pos = 4.8
        elif self.my_alien == 5:
            pos = 2
        elif self.my_alien == 4:
            pos = 0.1
        return pos
