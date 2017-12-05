row_number = input()
column_number = input()

class Content:
    pass
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