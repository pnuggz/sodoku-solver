import React from "react"
import { Row, Col } from "react-bootstrap"

import BoardRow from "./boardRow"

const Board = props => {
  const {homeState, dispatchHomeStateAction} = props

  const renderRows = () => {
    const rowsEl = []
    for(let i=0; i<9; i++) {
      rowsEl.push(
        <Row key={"row_" + i}>
          <BoardRow row_i={i} homeState={homeState} dispatchHomeStateAction={dispatchHomeStateAction} />
        </Row>
      )
    }
    return rowsEl
  }

  return (
    <React.Fragment>
      {renderRows()}
    </React.Fragment>
  )
}

export default Board