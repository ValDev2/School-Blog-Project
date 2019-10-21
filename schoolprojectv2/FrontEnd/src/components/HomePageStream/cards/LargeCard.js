import React, { Component } from 'react';
import './css/LargeCard.css';
import {Link} from 'react-router-dom';

class LargeCard extends Component {

  render(){
    return(
      <div className="LargeCard">
        <article className="Large-card-article">
          <div className="container">
            <Link to={`/article/${this.props.post.slug}`} alt="article-background" className="article-background"></Link>
            <div className="post-content">
              <div className="post-content-title-link">
                <Link to={`/article/${this.props.post.slug}`} className="post-title">
                  {this.props.post.title}
                </Link>
                <Link to={`/article/${this.props.post.slug}`} className="post-content-link">
                  {this.props.post.content.slice(0,20) + " ..."}
                </Link>
              </div>
              <div className="post-extra-infos">
                <div className="user-and-category">
                  <Link to={`/article/${this.props.post.slug}`} className="user-infos-username">
                    {this.props.post.user_name}
                  </Link>
                  <Link to={`/article/${this.props.post.slug}`} className="post-infos-category" style={{marginLeft: "5px"}}>
                    {this.props.post.category_subfield}
                  </Link>
                </div>
                <div className="post-time-infos">
                  <p className="time-infos">24 septembre</p>
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>
    );
  }
}

export default LargeCard;
