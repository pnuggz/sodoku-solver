import copy

class Board:
  def __init__(self):
    self.board = [
      [7, 2, 3, 0, 0, 0, 1, 5, 9],
      [6, 0, 0, 3, 0, 2, 0, 0, 8],
      [8, 0, 0, 0, 1, 0, 0, 0, 2],
      [0, 7, 0, 6, 5, 4, 0, 2, 0],
      [0, 0, 4, 2, 0, 7, 3, 0, 0],
      [0, 5, 0, 9, 3, 1, 0, 4, 0],
      [5, 0, 0, 0, 7, 0, 0, 0, 3],
      [4, 0, 0, 1, 0, 3, 0, 0, 6],
      [9, 3, 2, 0, 0, 0, 7, 1, 4]
    ]
    
    self.original = copy.deepcopy(self.board)
    self.attempts = []
    self.sections = []
    self.current_attempt = (0,0)

    for x in range(9):
      self.attempts.append([])
      for y in range(9):
        self.attempts[x].append([])
        self.attempts[x][y] = []

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
    if(self.original[y][x] == 0):
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
      if self.board[section[1]][section[0]] != 0:
        numbers.append(self.board[section[1]][section[0]])
    return numbers

  def get_row_numbers(self, x):
    numbers = []
    for y in range(9):
      if self.board[y][x] != 0:
        numbers.append(self.board[y][x])
    return numbers

  def get_column_numbers(self, y):
    numbers = []
    for x in range(9):
      if self.board[y][x] != 0:
        numbers.append(self.board[y][x])
    return numbers

  def get_next_number(self, x, y):
    attempts = self.attempts[y][x]
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
      if n in attempts:
        continue
      num = n
      break
    return num

  def reset_following_attempts(self, x, y):
   x += 1
   if x > 8:
     x = 0
     y += 1 
   for x_i in range(x,9):
    for y_i in range(y,9):
     self.attempts[y_i][x_i] = []

  def get_last_nonfixed(self, x, y):
    for attempts in range(10000):
      x -= 1
      if x < 0:
        x = 8
        y -= 1
      if self.is_fixed(x,y) == False:
        break
    return [x, y]

  def print_board(self,x,y):
    print(self.attempts[y][x])
    for y in range(9):
      print(self.board[y])


def main():
  board = Board()

  x = 0
  y = 0
  max_x = 0
  max_y = 0
  for attempts in range(100000000000):
    if x == 5 and y == 5:
      print(board.print_board(x,y))
      break
    print(attempts)
    if x > max_x and y > max_y:
      max_x = x
      max_y = y

    print(max_x,max_y)
    print((x,y))
    if board.is_fixed(x,y) == True:
      print(board.print_board(x,y))
      print('fixed')
      print('')
      x += 1
      if x > 8:
        x = 0
        y += 1

      if x == 8 and y == 8:
        print("Board is complete")
        break
      else:
        continue
    
    nex = board.get_next_number(x,y)
    # If there is no more numbers to try in this set
    if nex == None:
     # Reset this attempt and whatever is after
     board.board[y][x] = 0
     board.attempts[y][x] = []
     last_coord = board.get_last_nonfixed(x,y)
     x = last_coord[0]
     y = last_coord[1]
     board.reset_following_attempts(x,y)
     print(board.print_board(x,y))
     print('out of attempts')
     print('')
     continue

    board.board[y][x] = nex
    board.attempts[y][x].append(nex)
    print(board.print_board(x,y))
    print(nex)
    print('')
    x += 1
    if x > 8:
      x = 0
      y += 1

    if x == 8 and y == 8:
      print("Board is complete")
      break

if __name__ == '__main__':
  main()
