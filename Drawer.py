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
    BG_COLOR     = (60,  100, 200)

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

    def draw_content(self, content):
        options = {1 : Drawer.PINK_COLOR,
                   2 : Drawer.WHITE_COLOR,
                   3 : Drawer.GREEN_COLOR,
                   4 : Drawer.BLUE_COLOR,
                   5 : Drawer.RED_COLOR,
                   6 : Drawer.YELLOW_COLOR,
                   7 : Drawer.PURPLE_COLOR,
                   8 : Drawer.BROWN_COLOR,
                   9 : Drawer.LIGHT_GREEN_COLOR,
                   0 : Drawer.BG_COLOR}
        content = content.get_content()
        for row in range(len(content)):
            space = 1
            for column in range(len(content[0])):
                pygame.draw.rect(self._surface, options[content[row][column]], (210 + column * 30 + space * column, 60 + row*25 + space*row, 30, 25))
