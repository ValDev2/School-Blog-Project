import { GET_CATEGORY_TYPE } from '../actions/type';

const initState = {
  category_type: "",
  category_fields: []
}

export default function(state = initState, action){
  switch(action.type){
    case GET_CATEGORY_TYPE:
      console.log("LES TSATES TYPE ! ");
      console.log(state);
      console.log("PAYLOAD TYPE ! ");
      console.log(action.payload);
      return {
        ...initState,
        category_type: action.payload.category,
        category_fields: action.payload.category_fields
      }
    default:
      return state
  }
}
