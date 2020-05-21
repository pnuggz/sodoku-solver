class Board:
  def __init__(self):
    self.board = [
      [7, 6, 0, 0, 0, 0, 0, 8, 9],
      [0, 9, 0, 7, 6, 0, 0, 0, 1],
      [0, 1, 8, 4, 0, 0, 5, 0, 0],
      [0, 0, 0, 0, 7, 0, 2, 0, 4],
      [0, 7, 1, 2, 9, 4, 0, 0, 0],
      [0, 0, 4, 3, 1, 0, 0, 0, 8],
      [0, 0, 0, 0, 4, 3, 7, 0, 0],
      [9, 0, 0, 6, 0, 1, 0, 5, 3],
      [5, 0, 6, 0, 0, 0, 1, 0, 0]
    ]
    
    self.original = self.board
    self.attempts = []
    self.sections = []
    self.current_attempt = (0,0)

    for x in range(9):
      self.attempts.append([])
      for y in range(9):
        self.attempts[x].append([])
        self.attempts[x][y] = 0

    for sect in range(9):
      self.sections.append([])
    for x in range(9):
      for y in range(9):
        if x < 3:
          if y < 3:
            self.sections[0].append((x,y))
          elif y > 2 and y < 6:
            self.sections[3].append((x,y))
          else:
            self.sections[6].append((x,y))
        elif x > 2 and x < 6:
          if y < 3:
            self.sections[1].append((x,y))
          elif y > 2 and y < 6:
            self.sections[4].append((x,y))
          else:
            self.sections[7].append((x,y)) 
        else:
          if y < 3:
            self.sections[2].append((x,y))
          elif y > 2 and y < 6:
            self.sections[5].append((x,y))
          else:
            self.sections[6].append((x,y))

  def is_fixed(self, x, y):
    if(self.original[x][y] == 0):
      return False
    else:
      return True

  def get_section(self, x, y):
    for sect,arr in enumerate(self.sections):
      for tup in arr:
        if tup[0] == x and tup[1] == y:
          return sect

  def get_section_numbers(self, x, y):
    section = self.get_section(x, y)
    section_array = self.sections[section]
    numbers = []
    for section in section_array:
      if self.board[section[0]][section[1]] != 0:
        numbers.append(self.board[section[0]][section[1]])
    return numbers

  def get_row_numbers(self, x):
    numbers = []
    for y in range(9):
      if self.board[x][y] != 0:
        numbers.append(self.board[x][y])
    return numbers

  def get_column_numbers(self, y):
    numbers = []
    for x in range(9):
      if self.board[x][y] != 0:
        numbers.append(self.board[x][y])
    return numbers

  def get_next_number(self, x, y):
    section_num = self.get_section_numbers(x, y)
    row_num = self.get_row_numbers(x)
    col_num = self.get_column_numbers(y)
    num = None
    for n in range(1, 10):
      if n in section_num:
        continue
      if n in row_num:
        continue
      if n in col_num:
        continue
      num = n
    return num    


def main():
  board = Board()

  x = 0
  y = 0
  for attempts in range(1000):
    if board.is_fixed(x,y) == True:
      if x < 8:
        x += 1
      else:
        x = 0
        y += 1

      if x == 8 and y == 8:
        print("Board is complete")
        break
      else:
        continue
    
    


    if x < 8:
      x += 1
    else:
      x = 0
      y += 1

    if x == 8 and y == 8:
      print("Board is complete")
      break

if __name__ == '__main__':
  main()