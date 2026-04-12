import sys
import pygame


class Hero:
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        self.image = pygame.image.load(("images/minecraft_steve.png"))
        self.rect = self.image.get_rect()

        self.rect.center = self.screen_rect.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class GameCharacter:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Minecraft Steve")

        self.hero = Hero(self)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self._update_screen()

    def _update_screen(self):
        self.screen.fill((78, 159, 229))
        self.hero.blitme()
        pygame.display.flip()


if __name__ == "__main__":
    game = GameCharacter()
    game.run()
