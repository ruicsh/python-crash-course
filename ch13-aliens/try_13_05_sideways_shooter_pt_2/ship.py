import pygame


class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)
