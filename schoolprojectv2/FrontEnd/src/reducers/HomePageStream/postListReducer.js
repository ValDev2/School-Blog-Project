import {GET_POSTS_BY_CATEGORY} from "../../actions/type.js";

const initialState = {
  posts: [],
  isLoading: false,
}

//getting posts by category
function postListReducer(state = initialState, action){
  switch(action.type){
    case GET_POSTS_BY_CATEGORY:
      return {
        ...state,
        posts: action.payload,
        isLoading: true,
      };
    default:
      return state;
  }
}

export default postListReducer;
