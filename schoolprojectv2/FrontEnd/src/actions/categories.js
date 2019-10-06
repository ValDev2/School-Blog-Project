import axios from 'axios';
import { GET_CATEGORIES } from './type';
import { GET_CATEGORY_TYPE } from './type';

export const getCategories = () => dispatch => {
  axios.get('/categories/')
    .then( res => {
      console.log("API REQUEST !!!! ")
      console.log(res.data)
      dispatch({
        type: GET_CATEGORIES,
        payload: res.data
      });
    }).catch(err => console.log(err));
}

export const getCategoryFields = (category) => dispatch => {
  axios.get(`categories/${category}/`)
    .then( res => dispatch({
      type: GET_CATEGORY_TYPE,
      payload: res.data
    })).catch( err => console.log(err));
}
