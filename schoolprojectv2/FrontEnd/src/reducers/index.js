import posts from './posts';
import categories from './categories';
import categoryFields from './categoryFields';
import { combineReducers } from 'redux'

export default combineReducers({
  posts,
  categories,
  categoryFields,
});
