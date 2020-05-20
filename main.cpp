#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Board {
  public:
    vector <vector<int> > board;
    vector <vector<int> > board_section;
    vector <vector<int> > board_original;
    vector <vector <vector<int> > > attempted_values;
    void set_board ();
    int get_value(int x, int y);
    void set_value(int x, int y, int value);
    bool is_fixed(int x, int y);
    void set_attempted_values(int x, int y, int value);
    bool solution_attempted(int x, int y, int value);
};


bool Board::solution_attempted(int x, int y, int val) {
  vector<int> vec = attempted_values[x][y]
  int index = find(vec.begin(),vec.end(), value);
  if(index != vec.end()) {
    return true;
  } else {
    return false;
  }
}


void Board::set_attempted_values(int x, int y, int value) {
  attempted_values[x][y].push_back(value);
}


bool Board::is_fixed(int x, int y) {
  if(board_original[x][y] == 0) {
    return false;
  }
  return true;
}

void Board::set_value(int x, int y, int value) {
  board[x][y] = value;
}

int Board::get_value(int x, int y) {
  return board[x][y];
}

void Board::set_board() {
  int array[9][9] = {
    {7, 6, 0, 0, 0, 0, 0, 8, 9},
    {0, 9, 0, 7, 6, 0, 0, 0, 1},
    {0, 1, 8, 4, 0, 0, 5, 0, 0},
    {0, 0, 0, 0, 7, 0, 2, 0, 4},
    {0, 7, 1, 2, 9, 4, 0, 0, 0},
    {0, 0, 4, 3, 1, 0, 0, 0, 8},
    {0, 0, 0, 0, 4, 3, 7, 0, 0},
    {9, 0, 0, 6, 0, 1, 0, 5, 3},
    {5, 0, 6, 0, 0, 0, 1, 0, 0}
  };
  
  for (int x=0; x<9; x++) {
    vector<int> arr;
    vector <vector<int> > attempts;
    vector<int> empty;
    vector<int> section;
    for (int y=0; y<9; y++) {
      arr.push_back(array[x][y]);
      attempts.push_back(empty);

      
    }
    board.push_back(arr);
    board_original.push_back(arr);
    attempted_values.push_back(attempts);
  }
}


int next_possible_value(Board board, int x, int y) {
  int 
}


void solve(Board board) {
  for(int x=0; x<9; x++) {
    for(int y=0; y<9; y++) {
      bool is_fixed = board.is_fixed(x,y);
      if(is_fixed == true) {
        continue;
      }

      int n = next_possible_value(board, x, y);
    }
  }
}

int main() {
  Board board;
  board.set_board();
  board.get_value(1,1);

  solve(board);

  return 0;
}