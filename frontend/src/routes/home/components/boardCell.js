import React, {useState} from "react"
import { Row, Col } from "react-bootstrap"

const BoardCell = props => {
  const {row_i, col_i, homeState, dispatchHomeStateAction} = props
  const [isEditable, setIsEditable] = useState(false)

  const testDblClick = event => {
    setIsEditable(true)
  }
  
  const testBlur = event => {
    const board = homeState.board
    board[row_i][col_i] = event.target.value == 0 ? null :  event.target.value
    dispatchHomeStateAction({
      type: 'BOARD_UPDATE',
      payload: board
    })
    setIsEditable(false)
  }

  const testInput = event => {
    const inp = event.target.value
    if(inp == '') {
      return false
    }
    
    if(inp > 9) {
      event.target.value = 9
    } else if(inp < 0) {
      event.target.value = 0
    }
  }

  return (
    <React.Fragment>
      <div style={{width: '100%', height: '100%', border: '1px solid'}} onDoubleClick={event => testDblClick(event)} >
        {
          isEditable ? <input type="text" onBlur={event => testBlur(event)} autoFocus onInput={event => testInput(event)} style={{ width: '100%', position: 'absolute', top: '50%', transform: 'translateY(-50%)', textAlign: 'center' }} ></input> : 
            <div style={{ backgroundColor: 'red', width: '100%', position: 'absolute', top: '50%', transform: 'translateY(-50%)', textAlign: 'center' }}>{homeState.board[row_i][col_i]}</div>
        }
      </div>
    </React.Fragment>
  )
}

export default BoardCell