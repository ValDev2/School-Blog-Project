import categoryReducer from './categories/categories.js';
import {combineReducers} from 'redux';
import {homePageReducer} from './HomePageStream/homePageStreamReducer.js';
import {postReducer} from './singlePost/postReducer.js';
import{errorsReducer} from './Errors/errorsReducer.js';


export const rootReducer = combineReducers({
  categories: categoryReducer,
  homePage: homePageReducer,
  post: postReducer,
  errors: errorsReducer
});
