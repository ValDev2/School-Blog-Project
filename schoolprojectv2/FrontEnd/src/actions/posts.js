import axios from 'axios';
import { GET_POSTS } from './type';



export const getPosts = () => dispatch => {
  //getting all posts from the App
  //once we have the response, we will dispatch an action containing res.data
  axios.get('/posts/')
    .then( res => {
      dispatch({
        type: GET_POSTS,
        payload: res.data
      });
    }).catch(err => console.log(err));
};
