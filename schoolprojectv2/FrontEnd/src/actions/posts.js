import axios from 'axios';
import { GET_POSTS, GET_POST_BY_CATEGORY_TYPE } from './type';



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


export const getPostByCategoryType = (categoryType) => dispatch => {
  axios.get(`http://127.0.0.1:8000/posts/?categoryType=Sciences`)
    .then( res => {
      dispatch({
        type: GET_POST_BY_CATEGORY_TYPE,
        payload: res.data
    });
    console.log("API RES !!")
    console.log(res)
  }).catch( err => console.log(err))
}
