import sys
import pygame
from settings import Settings

class AlienInvasion:
    """gmae assets and behavior"""
    def __init__(self):
        """running game"""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_w, self.settings.screen_h)
            )
        pygame.display.set_caption("self.settings.name")

        self.bg

        self.running = True
        self.clock = pygame.time.Clock()

    def run_game(self):
        """game loop"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()
            self.clock.tick(self.setings.fps)

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()