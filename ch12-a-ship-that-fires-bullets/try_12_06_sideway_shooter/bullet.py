import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()
        self.settings = game.settings

        self.rect: pygame.Rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height
        )
        # +12 to align with the ship's nose
        self.rect.centery = game.ship.rect.centery + 12
        self.rect.left = game.ship.rect.right

        self.x = float(self.rect.x)

    def update(self):
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw(self):
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)
