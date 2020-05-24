import React from "react";

import HomeReducerBundle from "./homeReducer"
import { contexts } from "../../contexts"
import StateProviderGenerator from "../../lib/stateProviderGenerator"

import { HomeController } from "./homeController";

const Home = () => {
  const { initialState, homeReducer } = HomeReducerBundle
  const HomePageContext = contexts.homePage

  return (
    <StateProviderGenerator reducer={homeReducer} initialState={initialState} ContextName={HomePageContext}>
      <HomeController />
    </StateProviderGenerator >
  );
};

export default Home;
