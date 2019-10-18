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
                  Title !
                </a>
                <a href="#" className="small-post-content-link">
                  Content !
                </a>
              </div>
              <div className="small-post-extra-infos">
                <div className="small-user-and-category">
                  <a href="#" className="small-user-infos-username">
                    Valentin
                  </a>
                  <a href="#" className="small-post-infos-category" style={{marginLeft: "5px"}}>
                    Mathématiques ! 
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
