#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>

using namespace std;

class Board {
  public:
    int row_n = 9;
    int col_n = 9;
    vector <vector<int> > board = {  
      {8, 0, 0, 0, 0, 0, 0, 7, 0},
      {0, 6, 0, 0, 0, 0, 5, 0, 1},
      {0, 0, 0, 3, 1, 9, 6, 0, 0},
      {0, 0, 0, 0, 0, 0, 0, 0, 4},
      {0, 9, 8, 0, 0, 1, 0, 0, 0},
      {4, 0, 0, 2, 9, 5, 0, 0, 0},
      {0, 0, 1, 6, 0, 8, 0, 5, 0},
      {0, 3, 2, 0, 0, 0, 0, 8, 0},
      {6, 0, 9, 0, 0, 3, 0, 0, 0}
    };
    vector <vector <vector<int> > > attempts = {};

    void create_attempts_matrix() {
      vector <int> col = {};
      for(int x=0; x<col_n; x++) {
        vector <vector <int> > row = {};
        for(int y=0; y<col_n; y++) {
          row.push_back(col);
        }
        attempts.push_back(row);
      }
    };

    void create_section_fields() {
      for(int sect=0; sect<9; sect++) {
        sections.push_back({});
      }
      for(int x=0; x<col_n; x++) {
        for(int y=0; y<row_n; y++) {
          vector <int> coord = {x,y}; 
          if(x<3) {
            if(y<3) {
              sections[0].push_back(coord);
            } else if(y > 2 && y < 6) {
              sections[3].push_back(coord);
            } else {
              sections[6].push_back(coord);
            }
          } else if(x > 2 && x < 6) {
            if(y<3) {
              sections[1].push_back(coord);
            } else if(y > 2 && y < 6) {
              sections[4].push_back(coord);
            } else {
              sections[7].push_back(coord);
            }
          } else {
            if(y<3) {
              sections[2].push_back(coord);
            } else if(y > 2 && y < 6) {
              sections[5].push_back(coord);
            } else {
              sections[8].push_back(coord);
            }
          }
        }
      }
    };

    Board() {
      create_attempts_matrix();
      create_section_fields();
    }

    bool is_fixed(int x, int y) {
      if(original[y][x] == 0) {
        return false;
      }
      return true;
    }

    int get_section(int x, int y) {
      for(int sect=0; sect<9; sect++) {
        vector <vector <int> > arr = sections[sect];
        for(int i=0; i<arr.size(); i++) {
          vector <int> tup = arr[i];
          if(tup[0] == x && tup[1] == y) {
            return sect;
          }
        }
      }
      return 0;
    }

    vector <int> get_section_array(int x, int y) {
      int section_i = get_section(x, y);
      vector <vector<int> > section_array = sections[section_i];
      vector <int> numbers = {};
      for(int sect=0; sect<section_array.size(); sect++) {
        vector <int> section = section_array[sect];
        if(board[section[1]][section[0]] != 0) {
          numbers.push_back(board[section[1]][section[0]]);
        }
      }
      return numbers;
    }

    vector <int> get_row_array(int x) {
      vector <int> numbers = {};
      for(int y=0; y<row_n; y++) {
        if(board[y][x] != 0) {
          numbers.push_back(board[y][x]);
        }
      }
      return numbers;
    }

    vector <int> get_column_array(int y) {
      vector <int> numbers = {};
      for(int x=0; x<col_n; x++) {
        if(board[y][x] != 0) {
          numbers.push_back(board[y][x]);
        }
      }
      return numbers;
    }

    vector <int> get_empty_fields() {
      vector <int> numbers = {};
      for(int x=0; x<col_n; x++) {
        for(int y=0; y<row_n; y++) {
          if(board[y][x]== 0) {
            numbers.push_back(0);
          }
        }
      }
      return numbers;
    }

    int get_next_number(int x, int y) {
      vector <int> attempt = attempts[y][x];
      vector <int> section_num = get_section_array(x, y);
      vector <int> row_num = get_row_array(x);
      vector <int> col_num = get_column_array(y);
      int num = 0;
      for(int n=1; n<10; n++) {
        if(count(attempt.begin(), attempt.end(), n)) {
          continue;
        }
        if(count(section_num.begin(), section_num.end(), n)) {
          continue;
        }
        if(count(row_num.begin(), row_num.end(), n)) {
          continue;
        }
        if(count(col_num.begin(), col_num.end(), n)) {
          continue;
        }
        num = n;
        break;
      }
      return num;
    }

    vector <int> get_last_nonfixed(int x, int y) {
      for(int i=0; i<10000000; i++) {
        x = x - 1;
        if(x < 0) {
          x = 8;
          y = y - 1;
        }
        if(is_fixed(x,y) == false) {
          break;
        }
      }
      return {x,y};
    }

    bool check_duplicates(vector <int> arr) {
      for (std::size_t i = 0; i < arr.size(); ++i) {
        for (std::size_t j = i + 1; j < arr.size(); ++j) {
          if (arr[i] == arr[j])
            return true;
        }
      }
      return false;
    }

    void print_board() {
      for(int y=0; y<row_n; y++) {
        for(int x=0; x<col_n; x++) {
          cout << board[y][x] << " ";
        }
        cout << endl;
      }
    }

    bool check_complete(int x, int y) {
      if(y >= 8) {
        for(int x_i=0; x_i<col_n; x_i++) {
          for(int y_i=0; y_i<row_n; y_i++) {
            vector <int> section_num = get_section_array(x_i, y_i);
            vector <int> row_num = get_row_array(x_i);
            vector <int> col_num = get_column_array(y_i);
            vector <int> empty_fields = get_empty_fields();
            if(
              check_duplicates(section_num) == false &&
              check_duplicates(row_num) == false &&
              check_duplicates(col_num) == false &&
              empty_fields.size() == 0
            ) {
              return true;
            }
          }
        }
      }
      return false;
    }

    void set_board_value(int x, int y, int val) {
      board[y][x] = val;
    }

  private:
    vector <vector<int> > original = board;
    vector <vector <vector<int> > > sections = {};
    
};


vector <int> get_next_coordinates(int x, int y) {
  x = x + 1;
  if(x > 8) {
    x = 0;
    y = y + 1;
  }
  return {x,y};
}

int main() {
  Board board;

  int x = 0;
  int y = 0;
  for(int attempt=0; attempt<100000; attempt++) {
    if(board.check_complete(x,y) == true) {
      cout << "Board is Complete!" << endl;
      cout << "Number of attempt: " << attempt << endl;
      board.print_board();
      break;
    }

    if(board.is_fixed(x,y) == true) {
      vector <int> coord = get_next_coordinates(x,y);
      x = coord[0];
      y = coord[1];
      continue;
    }

    int n_next = board.get_next_number(x,y);
    if(n_next == 0) {
      board.board[y][x] = 0;
      board.attempts[y][x] = {};
      vector <int> coord_last = board.get_last_nonfixed(x,y);
      x = coord_last[0];
      y = coord_last[1];
    } else {
      board.board[y][x] = n_next;
      board.attempts[y][x].push_back(n_next);
      vector <int> coord = get_next_coordinates(x,y);
      x = coord[0];
      y = coord[1];
    }
  }
}

