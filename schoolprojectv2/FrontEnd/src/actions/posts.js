import {GET_POSTS_BY_CATEGORY} from './type';
import {GET_POST} from './type';
import {GET_ERRORS} from './type';
import axios from 'axios';

// Get the posts from the category
//Returns every single post for the moment ...
export const getPostsByCategory = category => dispatch => {
  axios.get(`http://127.0.0.1:8000/posts/?categoryType=${category}`)
    .then( res => {
      dispatch({
        type: GET_POSTS_BY_CATEGORY,
        payload: res.data
      })
    });
}

export const getPost = slug => dispatch => {
  axios.get(`http://127.0.0.1:8000/posts/${slug}`)
    .then( res => {
      dispatch({
        type: GET_POST,
        payload: res.data
      })
    })
    .catch(err => {
      const errors = {
        msg: err.response.data,
        status: err.response.status
      };
    })
    ;
}
