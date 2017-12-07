import pygame

class Drawer:
    PINK_COLOR   = (255, 155, 255)
    WHITE_COLOR  = (255, 255, 255)
    def __init__(self, surface):
        self._surface = surface

    def draw_field():
        pass
    
    def draw_text(self):
        font = pygame.font.Font(None, 36)
        game_title = font.render("PyGame", 1, Drawer.PINK_COLOR)
        font = pygame.font.Font(None, 20)
        remind = font.render("Press Space for rotate, Left for left move, Right for right move.", 1, Drawer.WHITE_COLOR)
        self._surface.blit(game_title, (10, 10))
        self._surface.blit(remind, (120, 30))

    def draw_content():
        pass