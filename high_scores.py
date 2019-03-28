import pygame
import pygame.font


class HighScores:
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.stats = stats
        self.screen_rect = screen.get_rect()
        self.bg_color = (0, 0, 0)

        self.prep_title()

        self.high_score = stats.high_score

    def prep_title(self):
        self.title = "High Scores"
        self.title_color = (255, 255, 255)
        self.title_font = pygame.font.SysFont(None, 79)
        self.title_width, self.title_height = 80, 50
        self.title_rect = pygame.Rect(560, 50, self.title_width, self.title_height)
        self.title_image = self.title_font.render(self.title, True, self.title_color)
        self.title_image_rect = self.title_image.get_rect()
        self.title_image_rect.center = self.title_rect.center

    def prep_scores(self):
        width, height = 540, 150
        at_most = 6

        self.scores = open("scores.txt", 'r')
        self.scores_color = (255, 255, 255)
        self.scores_font = pygame.font.SysFont(None, 60)
        self.scores_width, self.scores_height = 80, 50

        for line in self.scores:
            line = line.replace("\n", '')
            self.scores_rect = pygame.Rect(width, height, self.scores_width, self.scores_height)
            self.scores_image = self.scores_font.render(line, True, self.scores_color)
            self.scores_image_rect = self.scores_image.get_rect()
            self.scores_image_rect.center = self.scores_rect.center
            self.screen.blit(self.scores_image, self.scores_image_rect)
            height += 45
            at_most -= 1

            if at_most == 0:
                break

    def draw_scoreboard_screen(self):
        self.screen.fill(self.bg_color, self.screen_rect)
        self.screen.blit(self.title_image, self.title_image_rect)
        self.prep_scores()

    def print_scores(self):
        updated = open("scores.txt", 'r+')
        first_line = updated.readline()
        print(first_line)

    def update_scores(self):
        ''' Scores '''
        self.high_score = self.stats.high_score
        changed = False

        original = open("scores.txt", 'r')
        data = original.read()
        updatedfile = data

        for line in data:
            if self.high_score > int(line):
                updatedfile = str(self.stats.high_score) + "\n" + data
                changed = True
            break
        original.close()

        if changed:
            with open("scores.txt", 'w') as updated:
                updated.write(updatedfile)
            updated.close()
        self.stats.check_end_score = 0
        self.stats.game_over = False
