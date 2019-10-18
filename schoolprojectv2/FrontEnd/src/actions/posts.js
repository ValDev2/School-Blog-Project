import {GET_POSTS_BY_CATEGORY} from "./type";
import axios from 'axios';

// Get the posts from the category
//Returns every single post for the moment ...
export const getPostsByCategory = category => dispatch => {
  category = category.charAt(0).toUpperCase() + category.slice(1)
  axios.get(`http://127.0.0.1:8000/posts/?categoryType=${category}`)
    .then( res => {
      console.log(res)
      dispatch({
        type: GET_POSTS_BY_CATEGORY,
        payload: res.data
      })
    })
}
