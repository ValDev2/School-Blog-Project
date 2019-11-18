import {POST_ARTICLE} from '../../actions/type.js';

const initialState = {
  title: "",
  user: None,
  content: "",
  category: "Sciences",
  slug: ""
}

export function articleReducer(state=initialState, action){
  switch (action.type){
    case POST_ARTICLE:
      return {
        {...state},
        title: action.title,
        content: action.content,
        category: action.category,
      }

      
    default:
      return state;
  }
}
