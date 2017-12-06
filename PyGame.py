import time
import pygame

class Content:
    def __init__(self, row, column):
        self._content = [[0 for col in range(column)] for ro in range(row)]
        self._line = []
        self._fall_count = 0
        self._column = 0
        self._landed = False

    def add_line(self, column, ju):
        self._line = ju
        self._fall_count = 0
        self._column = column
        self._landed = False
    # It is a event need to be triggered by timer
    def step(self):
        if not self._landed:
            print self._fall_count
            if self._fall_count < len(self._line):
                for i in range(self._fall_count):
                    self._content[i][self._column] = self._line[-self._fall_count:][i]
            else:
                for i in range(len(self._line)):
                    self._content[i + self._fall_count - len(self._line)][self._column] = self._line[i]
                self._content[self._fall_count - len(self._line) - 1][self._column] = 0
            self._fall_count = self._fall_count + 1

        if self.isLanded():
            self._landed = True   

    # rotate the current falling line
    def rotate(self):
        print 'rotate'
        self._line = self._line[::-1]

    def clear_last_step(self, column):
        last_fall_count = self._fall_count
        if last_fall_count < len(self._line):
            for i in range(last_fall_count):
                self._content[i][column] = 0
        else:
            for i in range(len(self._line)):
                self._content[i + last_fall_count - len(self._line)][column] = 0

    def area_is_clear(self, column):
        is_clear = True
        last_fall_count = self._fall_count - 1
        if last_fall_count < len(self._line):
            for i in range(last_fall_count):
                if self._content[i][column] != 0:
                    is_clear = False
        else:
            for i in range(len(self._line)):
                if self._content[i + last_fall_count - len(self._line)][column] != 0:
                    is_clear = False
        return is_clear

    def left(self):
        if self.area_is_clear(self._column - 1):
            self._column = self._column - 1
            self._fall_count = self._fall_count - 1
            self.step()
            self.clear_last_step(self._column + 1)

    def right(self):
        if self.area_is_clear(self._column + 1):
            self._column = self._column + 1
            self._fall_count = self._fall_count - 1
            self.step()
            self.clear_last_step(self._column - 1)

    def erase_row(self, row):
        for column in range(len(self._content[0])):
            self._content[row][column] = 0
            for ro in range(row):
                self._content[row-ro][column] = self._content[row-ro-1][column]
            self._content[0][column] = 0

    def match_erase(self):
        for row in len(self._content):
            temp = self._content[row][0]
            isMatch = False
            for column in len(self._content[0]):
                if temp != self._content[row][column]:
                    isMatch = False
            isMatch = True
            if isMatch:
                self.erase_row(row)


    def printContent(self):
        for row in self._content:
            print row
        print ""
    
    def drawContent(self, window):
        for row in range(len(self._content)):
            for column in range(len(self._content[0])):
                if self._content[row][column] == 1:
                    pygame.draw.rect(window, (255,155,100), (210 + column *30, 60 + row*55, 30, 55))
                if self._content[row][column] == 2:
                    pygame.draw.rect(window, (255,100,100), (210 + column *30, 60 + row*55, 30, 55))
                if self._content[row][column] == 3:
                    pygame.draw.rect(window, (255,255,100), (210 + row *30, 60 + column*55, 30, 55))
                if self._content[row][column] == 4:
                    pygame.draw.rect(window, (255,55,100), (210 + row *30, 60 + column*55, 30, 55))

    def clear_content(self):
        row = len(self._content)
        column = len(self._content[0])
        self._content = [[0 for col in range(column)] for ro in range(row)]
        
    def isLanded(self):
        return len(self._content) < self._fall_count or self._content[self._fall_count-1][self._column] != 0 


class Field:
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def draw(self):
        for i in range(self._row):
            print "|" + 3*self._column*" " + "|"
        print "-" + 3*self._column*"-" + "-"

    

#row_number = input()
#column_number = input()
# f = Field(row_number, column_number)
# f.draw()
# while 1:
#     f.draw()
#     print ""
#     time.sleep(3)

# c = Content(4, 4)
# c.printContent()
# c.add_line(1, [2,4])
# c.step()
# c.printContent()
# c.step()
# c.printContent()
# c.step()
# c.printContent()
# c.step()
# c.printContent()
# c.step()
# c.printContent()
# c.step()
# c.printContent()

# c.add_line(3, [5, 2,4])
# c.step()
# c.printContent()
# c.step()
# c.printContent()
# c.rotate()
# c.step()
# c.printContent()

# print "left"
# c.left()
# c.printContent()

# c.step()
# c.printContent()
# c.step()
# c.printContent()
# c.step()
# c.printContent()
# c.step()
# print c.area_is_clear(2)
# print c.area_is_clear(1)
# c.printContent()
# Test erase row
# c.erase_row(3)
# c.printContent()
# c.erase_row(3)
# c.printContent()