import copy

class Board:
  def __init__(self):
    self.board = [
      [8, 0, 0, 0, 0, 0, 0, 7, 0],
      [0, 6, 0, 0, 0, 0, 5, 0, 1],
      [0, 0, 0, 3, 1, 9, 6, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 4],
      [0, 9, 8, 0, 0, 1, 0, 0, 0],
      [4, 0, 0, 2, 9, 5, 0, 0, 0],
      [0, 0, 1, 6, 0, 8, 0, 5, 0],
      [0, 3, 2, 0, 0, 0, 0, 8, 0],
      [6, 0, 9, 0, 0, 3, 0, 0, 0]
    ]
    
    self.original = copy.deepcopy(self.board)
    self.attempts = []
    self.sections = []

    self.create_attempts_matrix()
    self.create_section_fields()
  
  def create_section_fields(self):
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
            self.sections[8].append((x,y))

  def create_attempts_matrix(self):
    for x in range(9):
      self.attempts.append([])
      for y in range(9):
        self.attempts[x].append([])
        self.attempts[x][y] = []

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

  def get_section_array(self, x, y):
    section = self.get_section(x, y)
    section_array = self.sections[section]
    numbers = []
    for section in section_array:
      if self.board[section[1]][section[0]] != 0:
        numbers.append(self.board[section[1]][section[0]])
    return numbers

  def get_row_array(self, x):
    numbers = []
    for y in range(9):
      if self.board[y][x] != 0:
        numbers.append(self.board[y][x])
    return numbers

  def get_column_array(self, y):
    numbers = []
    for x in range(9):
      if self.board[y][x] != 0:
        numbers.append(self.board[y][x])
    return numbers

  def get_empty_fields(self):
    empty_fields = []
    for x in range(9):
      for y in range(9):
        if self.board[y][x] == 0:
          empty_fields.append(self.board[y][x])
    return empty_fields

  def get_next_number(self, x, y):
    attempts = self.attempts[y][x]
    section_num = self.get_section_array(x, y)
    row_num = self.get_row_array(x)
    col_num = self.get_column_array(y)
    num = None
    for n in range(1, 10):
      if n in (attempts + section_num + row_num + col_num):
        continue
      num = n
      break
    return num

  def get_last_nonfixed(self, x, y):
    for attempts in range(1000000):
      x -= 1
      if x < 0:
        x = 8
        y -= 1
      if self.is_fixed(x,y) == False:
        break
    return [x, y]

  def print_board(self,x,y):
    for y in range(9):
      print(self.board[y])

  def check_complete(self,x,y):
    if y >= 8:
      for x_i in range(9):
        for y_i in range(9):
          section_num = self.get_section_array(x_i, y_i)
          row_num = self.get_row_array(x_i)
          col_num = self.get_column_array(y_i)
          empty_fields = self.get_empty_fields()
          if check_duplicates(section_num) == False and check_duplicates(row_num) == False and check_duplicates(col_num) == False and len(empty_fields) == 0:
            return True
    return False


def check_duplicates(listOfElems):
  if len(listOfElems) == len(set(listOfElems)):
    return False
  else:
    return True


def get_next_coordinates(x,y):
  x += 1
  if x > 8:
    x = 0
    y += 1
  return [x,y]


def main():
  board = Board()

  x = 0
  y = 0
  for attempts in range(10000):
    # Check if complete
    is_complete = board.check_complete(x,y)
    if is_complete == True:
      print("Board is complete")
      print(attempts)
      board.print_board(x,y)
      break

    # If the field is pre-filled, skip
    if board.is_fixed(x,y) == True:
      coord = get_next_coordinates(x,y)
      x = coord[0]     
      y = coord[1]
      board.print_board(x,y)
      print('')
      continue
    
    # Get the next number for the field
    nex = board.get_next_number(x,y)
    # If there is no more numbers to try in this set
    if nex == None:
      # Reset this attempt and whatever is after
      board.board[y][x] = 0
      board.attempts[y][x] = []
      last_coord = board.get_last_nonfixed(x,y)
      x = last_coord[0]
      y = last_coord[1]
    else:
      # Update the board with the new number
      board.board[y][x] = nex
      board.attempts[y][x].append(nex)
      coord = get_next_coordinates(x,y)
      x = coord[0]     
      y = coord[1]
    board.print_board(x,y)
    print('')


if __name__ == '__main__':
  main()
