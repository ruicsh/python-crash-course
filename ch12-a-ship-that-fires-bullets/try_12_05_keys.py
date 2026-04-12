import sys
import pygame


class KeyStrokes:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.text_color = (30, 30, 30)
        self.bg_color = (78, 159, 229)
        self.font = pygame.font.SysFont(None, 48)

        self.text = ""

        self.prep_key()

    def prep_key(self):
        self.key_image = self.font.render(
            self.text, True, self.text_color, self.bg_color
        )
        self.key_rect = self.key_image.get_rect()
        self.key_rect.center = self.screen_rect.center

    def show(self):
        self.prep_key()
        self.screen.blit(self.key_image, self.key_rect)


class KeysGame:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Keys")

        self.keys = KeyStrokes(self)

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
                self.keys.text = "right"
            case pygame.K_LEFT:
                self.keys.text = "left"
            case pygame.K_UP:
                self.keys.text = "up"
            case pygame.K_DOWN:
                self.keys.text = "down"

    def _check_keyup_events(self, event):
        match event.key:
            case pygame.K_RIGHT:
                self.keys.text = ""
            case pygame.K_LEFT:
                self.keys.text = ""
            case pygame.K_UP:
                self.keys.text = ""
            case pygame.K_DOWN:
                self.keys.text = ""

    def _update_screen(self):
        self.screen.fill((78, 159, 229))
        self.keys.show()
        pygame.display.flip()


if __name__ == "__main__":
    game = KeysGame()
    game.run()
