import { GET_CATEGORIES } from '../../actions/type';

const initState = {
  categories: []
}

export default function categoryReducer(state = initState, action){
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
