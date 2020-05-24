import React, { useState, useEffect, useContext } from "react";

import { contextsState } from "../../contexts";

import { HomeViewer } from "./homeViewer";

export const HomeController = props => {
  const useStateValue = contextsState('homePage')
  const [homeState, dispatchHomeStateAction] = useStateValue()

  const [isLoading, setIsloading] = useState(true);

  useEffect(() => {
    setIsloading(false);
  }, []);

  const soln = () => {
    return new Promise(res => {
      setTimeout(() => {
        const arr = [
          [0,0,1,'forward'],
          [0,1,2,'forward'],
          [0,2,3,'forward'],
          [0,1,3,'backward']
        ]
        res(arr)
      }, 1000)
    })
  }

  const displayStep = (row_i, col_i, val, type) => {
    return new Promise(res => {
      setTimeout(() => {
        const board = homeState.board
        const board_fixed = homeState.board_fixed
        if(type == 'backward') {
          for(let row=row_i;row<9; row++) {
            const col_start = row == row_i ? col_i : 0
            for(let col=col_start;col<9; col++) {
              if(board_fixed[row][col] != null) {
                board[row][col] = null
              }
            }
          }
        }
        board[row_i][col_i] = val
        res(board)
      }, 500)
    })
  }

  const solveSudoku = async () => {
    const start_board = homeState.board
    await dispatchHomeStateAction({
      type: 'BOARD_FIXED_UPDATE',
      payload: start_board
    })
    console.log(homeState.board_fixed)

    const res = await soln()
    for(let i=0; i<res.length; i++) {
      const step = res[i]
      const [row_i,col_i,val,type] = step
      const board = await displayStep(row_i, col_i, val, type)
      dispatchHomeStateAction({
        type: 'BOARD_UPDATE',
        payload: board
      })
    };
  }

  return (
    <React.Fragment>
      <HomeViewer
        homeState={homeState}
        dispatchHomeStateAction={dispatchHomeStateAction}
        solveSudoku={solveSudoku}
        isLoading={isLoading}
      />
    </React.Fragment>
  );
};
