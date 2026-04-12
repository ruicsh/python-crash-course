import sys
import pygame


class Rocket:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load(("images/rocket.png"))
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += 1
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= 1
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= 1
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += 1

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class RocketGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Rocket")
        self.rocket = Rocket(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

            self._update_screen()

    def _check_keydown_events(self, event):
        match event.key:
            case pygame.K_RIGHT:
                self.rocket.moving_right = True
            case pygame.K_LEFT:
                self.rocket.moving_left = True
            case pygame.K_UP:
                self.rocket.moving_up = True
            case pygame.K_DOWN:
                self.rocket.moving_down = True

    def _check_keyup_events(self, event):
        match event.key:
            case pygame.K_RIGHT:
                self.rocket.moving_right = False
            case pygame.K_LEFT:
                self.rocket.moving_left = False
            case pygame.K_UP:
                self.rocket.moving_up = False
            case pygame.K_DOWN:
                self.rocket.moving_down = False

    def _update_screen(self):
        self.rocket.update()
        self.screen.fill((78, 159, 229))
        self.rocket.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    game = RocketGame()
    game.run()
