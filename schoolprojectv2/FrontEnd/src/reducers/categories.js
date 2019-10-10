import { GET_CATEGORIES } from '../actions/type';

const initState = {
  categories: []
}

export default function(state = initState, action){
  switch(action.type){
    case GET_CATEGORIES:
      return {
        ...state,
        categories: action.payload
      };
    default:
      return state;
  }
}
