import pygame

class Drawer:
    #              R      G     B
    PINK_COLOR   = (255, 155, 255)
    WHITE_COLOR  = (255, 255, 255)
    GREEN_COLOR  = (0,   255,   0)
    BLUE_COLOR   = (0,     0, 255)
    RED_COLOR    = (255,   0,   0)
    YELLOW_COLOR = (255, 255,   0)
    PURPLE_COLOR = (255,   0, 255)
    BROWN_COLOR  = (255, 153,  51)
    LIGHT_GREEN_COLOR  = (178, 255, 102)

    def __init__(self, surface):
        self._surface = surface

    def draw_field(self):
        pygame.draw.rect(self._surface, Drawer.GREEN_COLOR, (200, 50, 200, 400), 10)
    
    def draw_text(self):
        font = pygame.font.Font(None, 36)
        game_title = font.render("PyGame", 1, Drawer.PINK_COLOR)
        font = pygame.font.Font(None, 20)
        remind = font.render("Press Space for rotate, Left for left move, Right for right move.", 1, Drawer.WHITE_COLOR)
        self._surface.blit(game_title, (10, 10))
        self._surface.blit(remind, (120, 30))

    def draw_content():
        pass