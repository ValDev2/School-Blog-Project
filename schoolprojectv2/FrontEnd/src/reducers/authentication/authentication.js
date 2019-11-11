import {AUTH_START, AUTH_FAIL, AUTH_SUCESS, AUTH_LOGOUT} from '../../actions/type';


const initialState = {
  error_msg: [],
  error_status: null,
  token: null,
  loading: false
}

export function authenticationReducer(state = initialState, action){
  switch (action.type) {
    case AUTH_START:
      return {
        ...state,
        loading: true
      }
    case AUTH_SUCESS:
      return {
        ...state,
        error: null,
        token: action.token.key,
        loading: false
      }
    case AUTH_FAIL:
      let error_msg = [];
      for ( let key in action.payload.data){
        error_msg.push(action.payload.data[key]);
      }
      return {
        ...state,
        loading: false,
        error_msg: error_msg,
        error_status: action.payload.status
      }
    case AUTH_LOGOUT:
      return {
        loading: false,
        token: null,
        error: null,
        error_status: null
      }
    default:
      return state

  }
}
