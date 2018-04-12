import sys
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # initialize the game and creat a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # create a ship
    ship = Ship(ai_settings, screen)

    # begin the main loop of the game
    while True:
        # supervise keyboard and mouse event
        gf.check_event(ship)
        ship.update()
        # plot the screen again in every loop
        # make the screen lately plotted visiable
        gf.update_screen(ai_settings, screen, ship)

run_game()