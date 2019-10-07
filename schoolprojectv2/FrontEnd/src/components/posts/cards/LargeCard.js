import React, { Component } from 'react';
import './css/LargeCard.css';

class LargeCard extends Component {

  render(){
    return(
      <div className="LargeCard">
        <article className="Large-card-article">
          <div className="container">
            <a href="#" alt="article-background" className="article-background"></a>
            <div className="post-content">
              <div className="post-content-title-link">
                <a href="#" className="post-title">
                  Voici un super Titre pour ce post !
                </a>
                <a href="#" className="post-content-link">
                  On a besoin de faire des tests sur les composants pour être sûr qu'ils fonctionnet à marveille !
                </a>
              </div>
              <div className="post-extra-infos">
                <div className="user-and-category">
                  <a href="#" className="user-infos-username">
                    Valentin Fontanger :
                  </a>
                  <a href="#" className="post-infos-category" style={{marginLeft: "5px"}}>
                    Test
                  </a>
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

export default LargeCard
