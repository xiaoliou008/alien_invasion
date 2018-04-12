class Settings():
        """store all classes in <alien_invasion>"""

        def __init__(self):
            """initialize the game setting"""
            # screen settings
            self.screen_width = 1200
            self.screen_height = 650
            self.bg_color = (230, 230, 230)

            # ship settings
            self.ship_speed_factor = 1.5