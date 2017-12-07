import sys, pygame
from pygame.locals import *
from PyGame import *

class WindowField:
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def draw(self):
        for i in range(self._row):
            print "|" + 3*self._column*" " + "|"
        print "-" + 3*self._column*"-" + "-"

if __name__ == "__main__":
    pygame.init()
    clock = pygame.time.Clock() 
    window = pygame.display.set_mode((640, 480))
    x = 0
    y = 0
    count = 0
    pygame.display.set_caption("PyGame")
    content = Content(12, 6)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.__dict__['key'] == K_UP:
                    print 'add'
                    content.add_line(2, [1,2])
                if event.__dict__['key'] == K_r:
                    content.rotate()
                if event.__dict__['key'] == K_LEFT:
                    content.left()
                if event.__dict__['key'] == K_RIGHT:
                    content.right()

        #window.fill((60, 100, 200))
        pygame.draw.rect(window, (255,155,255), (200, 50, 200, 400), 10)
        pygame.display.update()
        clock.tick(30)
        count = count + 1
        if count == 100:
            print "step"
            count = 0
            content.step()
            content.printContent()
        content.drawContent(window)
