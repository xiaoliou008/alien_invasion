import pygame

class Ship():

    def __init__(self, screen):
        """initialize the ship and set its position"""
        self.screen = screen

        # load ship image and get its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # set every new ship in the middle bottom
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """plot the ship at the specified position"""
        self.screen.blit(self.image, self.rect)