import sys
import pygame

from settings import Settings
from ship import Ship

def run_game():
    # initialize the game and creat a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(screen)

    # begin the main loop of the game
    while True:
        # supervise keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # plot the screen again in every loop
        screen.fill(ai_settings.bg_color)
        ship.blitme()

        # make the screen lately plotted visiable
        pygame.display.flip()

run_game()