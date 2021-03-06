import sys, pygame
from pygame.locals import *
from PyGame import *
from Drawer import *
import random

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock() 
    window = pygame.display.set_mode((640, 480))
    # Use Drawer Class to deal with drawing
    drawer = Drawer(window)
    count = 0
    new_line = True
    pygame.display.set_caption("PyGame")
    content = Content(12, 6)
    window.fill(Drawer.BG_COLOR)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.__dict__['key'] == K_UP:
                    random_column = random.randint(0, 5)
                    random_list = random.sample(range(1, 9), random.randint(1,5))
                    content.add_line(random_column, random_list)
                if event.__dict__['key'] == K_SPACE:
                    content.rotate()
                if event.__dict__['key'] == K_LEFT:
                    content.left()
                if event.__dict__['key'] == K_RIGHT:
                    content.right()

        drawer.draw_text()
        drawer.draw_field()
        drawer.draw_content(content)
        pygame.display.update()
        clock.tick(30)
        count = count + 1
        if count == 100:
            count = 0
            content.step()
            # new line will be created in the next step after landed
            if new_line:
                random_column = random.randint(0, 5)
                random_list = random.sample(range(1, 9), random.randint(1,5))
                content.add_line(random_column, random_list)
            if content.is_landed():
                new_line = True
            else:
                new_line = False

        if content.is_landed():
            pygame.draw.line(window, Drawer.YELLOW_COLOR, (210, 418), (390, 418), 6) 
        else:
            pygame.draw.line(window, Drawer.BG_COLOR, (210, 418), (390, 418), 6)