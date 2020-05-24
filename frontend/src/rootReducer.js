import { globalReducerBundle } from "./globalReducer";

export const initialState = {
  globalState: globalReducerBundle.initialState,
};

export const rootReducer = ({ globalState }, action) => ({
  globalState: globalReducerBundle.globalReducer(globalState, action),
});
