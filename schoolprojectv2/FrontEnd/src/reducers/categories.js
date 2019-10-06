import { GET_CATEGORIES } from '../actions/type';

const initState = {
  categories: []
}

export default function(state = initState, action){
  switch(action.type){
    case GET_CATEGORIES:
      console.log("PAYLOAD ! !! ");
      console.log(action.payload);
      return {
        ...state,
        categories: action.payload
      };
    default:
      console.log("DEFAULT STATE §!!! ")
      console.log(state)
      return state;
  }
}
