import pygame

from settings import Settings
from start_screen import Start
from high_scores import HighScores
from scoreboard import Scoreboard
from stats import GameStats
from ship import Ship
from UFO import UFO
from events import Update
from bullet_animations import BulletAnimation
from collisions import Collisions

from pygame.sprite import Group


def run_game():
    # Initialize game
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invaders by Diana Joya")

    # Game Stats
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Screens
    start_screen = Start(ai_settings, screen)
    score_board = HighScores(ai_settings, screen, stats)

    # Sprite Groups
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    bunkers = Group()
    random_ufo = UFO(ai_settings, screen)
    bullet_animation = BulletAnimation(ai_settings, screen, ship, bullets, aliens, stats, sb, random_ufo, bunkers)

    events = Update(ai_settings, screen, ship, bullets, aliens, stats, sb, start_screen, score_board, random_ufo,
                    bunkers)
    collision = Collisions(ai_settings, screen, ship, bullets, aliens, stats, sb, start_screen, score_board, random_ufo,
                           bunkers)

    # Game Loop
    while True:
        events.check_events()

        if stats.game_active:
            current_time = pygame.time.get_ticks()
            ship.update()
            bullet_animation.update_bullets()
            collision.update_aliens()
            bunkers.update()
            if ai_settings.ufo_allowed:
                random_ufo.update(current_time)

        events.update_screen()


run_game()
