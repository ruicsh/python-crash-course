import sys
import random

import pygame
from pygame.sprite import Sprite


class Raindrop(Sprite):
    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/raindrop.png")
        self.rect: pygame.Rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += 1
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)


class Raindrops:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Raindrops")

        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.raindrops = pygame.sprite.Group()
        self._create_raindrops()

    def run(self):
        self._create_raindrops()

        while True:
            self.raindrops.update()
            self._update_raindrops()
            self._check_events()
            self._update_screen()

            if len(self.raindrops) == 0:
                sys.exit()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_raindrops(self):
        rd = Raindrop(self)
        rd_width, rd_height = rd.rect.size

        current_x, current_y = rd_width, rd_height
        while current_y < self.screen_rect.height - rd_height:
            while current_x < self.screen_rect.width - rd_width:
                self._create_raindrop(current_x, current_y)
                current_x += 2 * rd_width

            current_x = rd_width
            current_y += 2 * rd_height

    def _create_raindrop(self, x, y):
        x = random.randint(-30, 30) + x
        y = random.randint(-30, 30) + y

        new_raindrop = Raindrop(self)
        new_raindrop.x = x
        new_raindrop.y = y
        new_raindrop.rect.x = x
        new_raindrop.rect.y = y
        self.raindrops.add(new_raindrop)

    def _update_raindrops(self):
        for rd in self.raindrops.sprites():
            if rd.rect.top > self.screen_rect.bottom:
                self.raindrops.remove(rd)

    def _update_screen(self):
        self.screen.fill((60, 60, 60))
        for rd in self.raindrops.copy():
            rd.draw()
        pygame.display.flip()


if __name__ == "__main__":
    game = Raindrops()
    game.run()
