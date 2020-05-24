import { createContext, useContext } from "react"

export const contexts = {
  global: createContext(),
  homePage: createContext()
}

export const contextsState = (contextName) => {
  return () => useContext(contexts[contextName])
}