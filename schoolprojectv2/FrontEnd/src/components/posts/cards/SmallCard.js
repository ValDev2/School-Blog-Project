import React, { Component } from 'react';
import './css/SmallCard.css';

export default class SmallCard extends Component {

  render(){
    return(
      <div className="SmallCard">
        <article className="Small-card-article">
          <div className="small-container">
            <a href="#" alt="article-background" className="article-background-small"></a>
            <div className="post-content-small">
              <div className="small-post-content-title-link">
                <a href="#" className="small-post-title">
                  {this.props.title}
                </a>
                <a href="#" className="small-post-content-link">
                  {this.props.content}
                </a>
              </div>
              <div className="small-post-extra-infos">
                <div className="small-user-and-category">
                  <a href="#" className="small-user-infos-username">
                    {this.props.user_name} in 
                  </a>
                  <a href="#" className="small-post-infos-category" style={{marginLeft: "5px"}}>
                    {this.props.category_subfield}
                  </a>
                </div>
              </div>
            </div>
          </div>
        </article>
      </div>
    )
  }
}
