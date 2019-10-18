import axios from 'axios';
import { GET_CATEGORIES } from './type';

//Getting all Categories
export const getCategories = () => dispatch => {
  axios.get('/categories/')
    .then( res => {
      dispatch({
        type: GET_CATEGORIES,
        payload: res.data
      });
    }).catch(err => console.log(err));
}
