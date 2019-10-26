import {GET_ERRORS} from '../../actions/type';

const initialState = {
  msg: [],
  status: null
}

export function errorsReducer(state = initialState, action){
  switch(action.type) {
    case GET_ERRORS:
      console.log(action.payload.msg);
      return {
        ...state,
        msg: action.payload.msg,
        status: action.payload.status
      }
    default:
      return state;
  }
}
