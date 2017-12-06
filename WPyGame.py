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
   pygame.display.set_caption("PyGame")
   while True:
       for event in pygame.event.get():
           if event.type == KEYUP or event.type == QUIT:
               pygame.quit()

       window.fill((60, 100, 200))
       pygame.draw.rect(window, (255,155,255), (200, 50, 200, 400), 10)
       pygame.draw.rect(window, (255,155,100), (201, 51, 30, 55))
       pygame.display.update()
       clock.tick(30)
