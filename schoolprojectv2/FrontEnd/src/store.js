import { createStore, applyMiddleware, compose } from 'redux';
import thunk from 'redux-thunk';
import rootReducers from './reducers';
const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
//initialising states

const initialState = {posts: []}
const middleware = [thunk]
//defining the store
export const store = createStore(
  rootReducers,
  initialState,
  composeEnhancers(
    applyMiddleware(...middleware)
  )
);
