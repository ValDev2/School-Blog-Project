import axios from 'axios';
import {AUTH_START, AUTH_FAIL, AUTH_SUCESS, AUTH_LOGOUT, GET_ERRORS} from './type';


export const authStart = () => {
  return {
    type: AUTH_START,
    loading: true
  };
}

export const authSucess = token => {
  console.log(token);
  return {
    type: AUTH_SUCESS,
    token: token,
    error: null,
    loading: false
  };
}

export const authFail = error => {
  return {
    type: AUTH_FAIL,
    payload: error
  };
}


export const logout = () => {
  window.localStorage.removeItem('token');
  window.localStorage.removeItem('expiration_time');
  return {
    type: AUTH_LOGOUT
  }
}


export const authLogout = () => dispatch => {
  axios.post('http://127.0.0.1:8000/rest-auth/logout/',{})
  .then( res => {
    dispatch(logout());
    console.log("LOGOUT !!!!!!!")
  })
  .catch(err => console.log(err))
}


export const checkAuthTimeOut = expiration_time => dispatch => {
  return setTimeout(()=> {
    dispatch(logout());
  }, expiration_time * 1000);
}


export const authLogin = (email, password) => dispatch => {
  dispatch(authStart());
  axios.post('http://127.0.0.1:8000/rest-auth/login/',{
      "email": email,
      "password": password
  })
  .then( res => {
    const token = res.data
    const expiration_time = new Date(new Date().getTime() + 3600 * 1000);
    window.localStorage.setItem('token', token);
    window.localStorage.setItem('expiration_time', expiration_time);
    dispatch(authSucess(token));
    dispatch(checkAuthTimeOut(3600));
  })
  .catch( error => {
    dispatch(authFail(error.response));
  })
}

export const authStateCheck = () => dispatch => {
  const expiration_time = window.localStorage.getItem('expiration_time');
  const token = window.localStorage.getItem('token');
  if (!token){
    return dispatch(logout());
  } else if ( expiration_time <= new Date()){
    return dispatch(logout());
  } else {
    return checkAuthTimeOut((expiration_time - new Date().getTime()) / 1000)
  }
}
