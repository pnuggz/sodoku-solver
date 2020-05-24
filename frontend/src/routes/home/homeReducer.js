import { combineReducers } from "../../lib/combineReducers";


const board = () => {
  const board = []
  for(let y=0; y<9; y++) {
    const row = []
    for (let x=0; x<9; x++) {
      row.push(null)
    }
    board.push(row)
  }
  return board
}


const initialState = {
  board: board(),
  board_fixed: board()
};

const boardReducer = (state, action) => {
  switch (action.type) {
    case "BOARD_UPDATE":
      return {
        ...state,
        board: action.payload
      };
    case "BOARD_FIXED_UPDATE":
      return {
        ...state,
        board_fixed: action.payload
      };

    default:
      return state;
  }
};

const homeReducer = combineReducers(boardReducer);

const HomeReducerBundle = {
  initialState: initialState,
  homeReducer: homeReducer
};

export default HomeReducerBundle