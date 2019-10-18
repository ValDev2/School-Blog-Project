import { combineReducers } from 'redux';
import postListReducer from './postListReducer';

export const homePageReducer = combineReducers({
  postList: postListReducer
});
