import React, { Component } from 'react';
import { connect } from 'react-redux';
import './css/StreamCardItem.css';

export default class StreamCardItem extends Component {

  render(){
    return(
      <div className="StreamCardItem">
        <article className="StreamPostPreview">
          <div className="StreamCardItemContent">
            <div className="StreamCardUpperContent">
              <a href="#" className="StreamLink">
                <h2 className="StreamCardItemTitle">
                  {this.props.title}
                </h2>
                <p className="StreamCardItemSubTitle">
                  {this.props.content}
                </p>
              </a>
            </div>
            <div className="StreamCardLowerContent">
            <a href="#" className="StreamLink">
              <div className="StreamCardInfo">
                <span className="StreamCardUser">ValentinF</span> dans <span className="StreamCardCategory">Mathématiques</span>
              </div>
            </a>
            </div>
          </div>
          <a className="StreamCardItemBackground" href="#"></a>
        </article>
      </div>
    )
  }
}
