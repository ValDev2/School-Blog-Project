import React, { Component } from 'react';
import './css/SmallCard.css';
import {Link} from 'react-router-dom';

export default class SmallCard extends Component {

  render(){
    return(
      <div className="SmallCard">
        <article className="Small-card-article">
          <div className="small-container">
            <Link to={`/article/${this.props.post.slug}`} alt="article-background" className="article-background-small"></Link>
            <div className="post-content-small">
              <div className="small-post-content-title-link">
                <Link to={`/article/${this.props.post.slug}`} className="small-post-title">
                  {this.props.post.title}
                </Link>
                <Link to={`/article/${this.props.post.slug}`} className="small-post-content-link">
                  {this.props.post.content.slice(0,20) + " ..."}
                </Link>
              </div>
              <div className="small-post-extra-infos">
                <div className="small-user-and-category">
                  <Link to={`/article/${this.props.post.slug}`} className="small-user-infos-username">
                    {this.props.post.user_name}
                  </Link>
                  <Link to={`/article/${this.props.post.slug}`} className="small-post-infos-category" style={{marginLeft: "5px"}}>
                    {this.props.post.category_subfield}
                  </Link>
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>
    )
  }
}
