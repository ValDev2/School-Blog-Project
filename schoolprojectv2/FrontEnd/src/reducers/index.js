import categoryReducer from './categories/categories.js';
import {combineReducers} from 'redux';
import {homePageReducer} from './HomePageStream/homePageStreamReducer.js';
import {postReducer} from './singlePost/postReducer.js';
import {authenticationReducer} from './authentication/authentication.js';


export const rootReducer = combineReducers({
  categories: categoryReducer,
  homePage: homePageReducer,
  post: postReducer,
  authentication: authenticationReducer
});
