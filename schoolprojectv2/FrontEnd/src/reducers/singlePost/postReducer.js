import {GET_POST} from '../../actions/type.js';

const initialState = {
  post: {},
  isLoading: false
}

export function postReducer(state=initialState, action){
  switch(action.type){
    case GET_POST:
      return {
        ...state,
        post: action.payload,
        isLoading: true
      };
    default:
      return state;
  }
}
