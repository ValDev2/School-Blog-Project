import categoryReducer from './categories/categories.js';
import {combineReducers} from 'redux';
import {homePageReducer} from './HomePageStream/homePageStreamReducer.js';

export const rootReducer = combineReducers({
  categories: categoryReducer,
  homePage: homePageReducer
});
