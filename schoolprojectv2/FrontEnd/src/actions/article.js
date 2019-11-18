import {POST_ARTICLE, PUBLISH_START} from './type.js';


export const articlePublishStart = () => {
  type: PUBLISH_START,
  loading: true
}

export const articlePublishSucess = article => {
  type: PUBLISH_SUCESS,
  loading: false,
  article: article,
  error: null
}

export const articlePublishFail = error => {
  type: PUBLISH_FAIL,
  loading: false,
  aritlce: None,
  error: error
}
