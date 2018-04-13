import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """a class managing bullet"""

    def __init__(self, ai_settings, screen, ship):
        """create a bullet object at the ship's position"""
        super().__init__()
        self.screen = screen

        # create a rectanble at (0,0) to represent bullet and set right position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store bullet's position
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """bullet move up"""
        # update the value that show the position of the bullet
        self.y -= self.speed_factor
        # update the position of rect
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)