import time
row_number = input()
column_number = input()


class Content:
    def __init__(self):
        _content = []
        _line = []
        _fall_count = 0
        _column = 0

    def add_line(self, column, ju):
        self._line = ju
        self._fall_count = 0
        self._column = column
    
    def step():
        self._content[self._column] = self._line[-1:]
        self._fall_count = self._fall_count + 1   

class Field:
    def __init__(self, row, column):
        self._row = row
        self._column = column

    def draw(self):
        for i in range(self._row):
            print "|" + 3*self._column*" " + "|"
        print "-" + 3*self._column*"-" + "-"

f = Field(row_number, column_number)
f.draw()
while 1:
    f.draw()
    print ""
    time.sleep(3)