import { GET_POSTS } from '../actions/type';

//useless
const initState = {posts: []}

export default function(state = initState, action){
  switch(action.type){
    case GET_POSTS:
      //Comment unpack initalState
      return action.payload
    default:
      return state
  }
}
