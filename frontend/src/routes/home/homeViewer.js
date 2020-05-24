import React from "react";
import posed from "react-pose";
import { Row, Col } from "react-bootstrap"

import { PageLayout } from "../../modules/pageLayout/index";

import Board from "./components/board"

const posedDivConfig = {
  preLoad: {
    x: "-100%"
  },
  loaded: {
    x: 0
  }
};

const ParentDiv = posed.div(posedDivConfig);

export const HomeViewer = props => {
  const { homeState, dispatchHomeStateAction, isLoading, solveSudoku } = props

  return (
    <PageLayout>
      <ParentDiv pose={isLoading ? "preLoad" : "loaded"}>
        <Row>
          <Col style={{ textAlign: 'center' }}>
            <h1>SUDOKU SOLVER</h1>
          </Col>
        </Row>
        <Row>
          <Col>
            <Board homeState={homeState} dispatchHomeStateAction={dispatchHomeStateAction} />
          </Col>
        </Row>
        <Row>
          <Col style={{ textAlign: 'center', paddingTop: '1em' }}>
            <button className="button" onClick={() => solveSudoku()}>SOLVE</button>
          </Col>
        </Row>
      </ParentDiv>
    </PageLayout>
  );
};
