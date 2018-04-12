import sys
import pygame

def check_event():
    """react to keyboard and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """update the image on the screen and switch to the new screen"""
    # replot the screen in every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # make the screen lately plotted visiable
    pygame.display.flip()