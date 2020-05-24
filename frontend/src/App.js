import React from "react";
import { Router, Switch, Route } from "react-router-dom";
import posed, { PoseGroup } from "react-pose";

import history from "./lib/history";
import { StateProvider } from "./lib/state";

import { initialState, rootReducer } from "./rootReducer";

import 'bootstrap/dist/css/bootstrap.min.css';
import "./styles/index.css";

import { Home } from "./routes/home";

const RouteContainer = posed.div({
  enter: { opacity: 1, delay: 300, beforeChildren: true },
  exit: { opacity: 0 }
});

const App = () => {
  return (
    <StateProvider initialState={initialState} reducer={rootReducer}>
      <Router history={history}>
        <Route
          render={({ location }) => (
            <React.Fragment>
              <PoseGroup>
                <RouteContainer key={location.pathname}>
                  <Switch location={location}>
                    <Route exact={true} path="/" render={() => <Home />} />
                  </Switch>
                </RouteContainer>
              </PoseGroup>
            </React.Fragment>
          )}
        />
      </Router>
    </StateProvider>
  );
};

export default App;
