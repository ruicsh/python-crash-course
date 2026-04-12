import sys
import pygame


class BlueSky:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Blue Sky")

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()

    def _update_screen(self):
        self.screen.fill((78, 159, 229))
        pygame.display.flip()


if __name__ == "__main__":
    game = BlueSky()
    game.run()
