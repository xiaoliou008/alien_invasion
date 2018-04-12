import sys

import pygame

def run_game():
    # initialize the game and creat a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 650))
    pygame.display.set_caption("Alien Invasion")

    # set the backgroung color
    bg_color = (230, 230, 230)

    # begin the main loop of the game
    while True:
        # supervise keyboard and mouse event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # plot the screen again in every loop
        screen.fill(bg_color)
        
        # make the screen lately plotted visiable
        pygame.display.flip()

run_game()