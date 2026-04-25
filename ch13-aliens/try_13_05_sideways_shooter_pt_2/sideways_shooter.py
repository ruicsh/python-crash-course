import sys
import pygame

from settings import Settings
from ship import Ship
from bullet import Bullet


class SidewaysShooter:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Sideways Shooter")
        self.screen = pygame.display.set_mode((1200, 800))
        self.screen_rect = self.screen.get_rect()

        self.settings = Settings()
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

    def run(self):
        while True:
            for event in pygame.event.get():
                match event.type:
                    case pygame.QUIT:
                        sys.exit()
                    case pygame.KEYDOWN:
                        self._check_keydown_events(event)
                    case pygame.KEYUP:
                        self._check_keyup_events(event)

            self._update_bullets()
            self._update_screen()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen_rect.right:
                self.bullets.remove(bullet)

    def _check_keydown_events(self, event):
        match event.key:
            case pygame.K_UP | pygame.K_k:
                self.ship.moving_up = True
            case pygame.K_DOWN | pygame.K_j:
                self.ship.moving_down = True
            case pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self, event):
        match event.key:
            case pygame.K_UP | pygame.K_k:
                self.ship.moving_up = False
            case pygame.K_DOWN | pygame.K_j:
                self.ship.moving_down = False

    def _update_screen(self):
        self.screen.fill((78, 159, 229))
        for bullet in self.bullets.sprites():
            bullet.draw()
        self.ship.update()
        self.ship.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    # Make a game instance, and run the game.
    game = SidewaysShooter()
    game.run()
