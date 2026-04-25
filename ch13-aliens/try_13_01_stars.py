import sys
import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, game):
        super().__init__()

        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load("images/star.png")
        self.rect: pygame.Rect = self.image.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        self.screen.blit(self.image, self.rect)


class StarsGame:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Stars")

        self.screen = pygame.display.set_mode((1_200, 800))
        self.screen_rect = self.screen.get_rect()

        self.stars = pygame.sprite.Group()

    def run(self):
        star = Star(self)
        star_width, star_height = star.rect.size

        current_x, current_y = star_width, star_height
        while current_y < (self.screen_rect.height - star_height):
            while current_x < (self.screen_rect.width - star_width):
                self._create_star(current_x, current_y)
                current_x += 2 * star_width

            current_x = star_width
            current_y += 2 * star_height

        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def _create_star(self, x_position, y_position):
        new_star = Star(self)
        new_star.x = x_position
        new_star.y = y_position
        new_star.rect.x = x_position
        new_star.rect.y = y_position
        self.stars.add(new_star)

    def _update_screen(self):
        self.screen.fill((60, 60, 60))
        for star in self.stars.sprites():
            star.draw()
        pygame.display.flip()


if __name__ == "__main__":
    game = StarsGame()
    game.run()
