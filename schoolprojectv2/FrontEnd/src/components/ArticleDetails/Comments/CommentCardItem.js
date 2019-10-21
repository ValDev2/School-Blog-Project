import React, {Component} from 'react';
import './css/CommentCardItem.css';

class CommentCardItem extends Component {
  render(){
    return(
      <div className="CommentCardItem">
        <div className="CommentCardItemContainer">
          <div className="CommentCardItemHeader">
            <a href="#" className="CommentCardItemUser">Valentin</a>
            <p className="CommentCardItemTime">17 Oct</p>
          </div>
          <div className="CommentCardItemResponse">
            <p> Alors oui c'est un excellent Commentaire blablablablballa ! </p>
          </div>
          <div className="CommentCardItemSocialInfos">
            <div className="CommentCardItemLikes">
              <i className="fab fa-gratipay"></i>
              <span className="CommentCardItemLikesNumber">
                300 likes
              </span>
            </div>
            <div className="CommentCardItemActions">
              <span className="CommentCardItemResponse">
                Reponse
              </span>
            </div>
          </div>
        </div>
      </div>
    )
  }
}


export default CommentCardItem;
