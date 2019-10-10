import { GET_POSTS, GET_POST_BY_CATEGORY_TYPE } from '../actions/type';

//useless
const initState = {posts: []}

export default function(state = initState, action){
  switch(action.type){
    case GET_POSTS:
      //Comment unpack initalState
      return action.payload
    case GET_POST_BY_CATEGORY_TYPE:
      console.log("PAYLOAD : ")
      console.log(action.payload);
      return action.payload
    default:
      return state
  }
}
