import React from "react"
import { Row, Col } from "react-bootstrap"

import BoardCell from "./boardCell"

const BoardRow = props => {
  const {row_i, homeState, dispatchHomeStateAction} = props

  const renderCells = () => {
    const cellEls = []
    for(let i=0; i<9; i++) {
      cellEls.push(
        <Col key={"col_" + i} style={{ padding: 0, height: '5em' }}>
          <BoardCell row_i={row_i} col_i={i} homeState={homeState} dispatchHomeStateAction={dispatchHomeStateAction} />
        </Col>
      )
    }
    return cellEls
  }

  return (
    <React.Fragment>
      {renderCells()}
    </React.Fragment>
  )
}

export default BoardRow