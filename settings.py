class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        ''' Ship '''
        self.ship_limit = 3
        self.explode = False

        ''' Bullet '''
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        ''' Aliens '''
        self.fleet_drop_speed = 3
        self.ufo_allowed = True
        self.ufo_explode = False
        self.alien_explosion = False
        self.alien_bullets_allowed = 2
        self.alien_bullet_speed_factor = 2
        self.alien_score = 10

        ''' Game Settings '''
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.ufo_speed_factor = 2
        self.fleet_direction = 1
        self.alien_bullet_speed_factor = 2

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ufo_speed_factor *= self.speedup_scale
