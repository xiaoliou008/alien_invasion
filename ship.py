import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """initialize the ship and set its position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # load ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set every new ship in the middle bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store float in ship.center
        self.center = float(self.rect.centerx)
        # moving flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """adjust the ship's position due to moving flag"""
        # update ship's center value instead of rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        # update rect object due to self.center
        self.rect.centerx = self.center

    def blitme(self):
        """plot the ship at the specified position"""
        self.screen.blit(self.image, self.rect)