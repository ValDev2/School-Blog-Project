import React, {Component} from 'react';
import CommentCardItem from './CommentCardItem.js';
import './css/CommentsBox.css';

class CommentsBox extends Component {
  render(){
    return(
      <div className="CommentBox">
        <div className="CommentBoxContainer">
          <div className="CommentBoxResponses">
            <span className="CommentBoxHeaderTitle">
              Commentaires
            </span>
            <div className="CommentBoxResponsesList">
              {this.props.comments.map( cmt => (
                <CommentCardItem comment={cmt} />
              ))}
            </div>
          </div>
        </div>
      </div>
    )
  }
}

export default CommentsBox;
