import sys
import pygame

def check_event(ship):
    """react to keyboard and mouse event"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # ship move right
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                # ship move left
                ship.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                ship.moving_left = False

def update_screen(ai_settings, screen, ship):
    """update the image on the screen and switch to the new screen"""
    # replot the screen in every loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    
    # make the screen lately plotted visiable
    pygame.display.flip()