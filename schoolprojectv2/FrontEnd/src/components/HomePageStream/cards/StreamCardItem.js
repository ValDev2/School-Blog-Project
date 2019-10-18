import React, { Component } from 'react';
import { connect } from 'react-redux';
import './css/StreamCardItem.css';
import { Link } from 'react-router-dom';


export default class StreamCardItem extends Component {

  render(){
    return(
      <div className="StreamCardItem">
        <article className="StreamPostPreview">
          <div className="StreamCardItemContent">
            <div className="StreamCardUpperContent">
              <Link to={`/article/${this.props.id}`} className="StreamLink">
                <h2 className="StreamCardItemTitle">
                  {this.props.title}
                </h2>
                <p className="StreamCardItemSubTitle">
                  {this.props.content}
                </p>
              </Link>
            </div>
            <div className="StreamCardLowerContent">
            <Link to={`/article/${this.props.id}`} className="StreamLink">
              <div className="StreamCardInfo">
                <span className="StreamCardUser">ValentinF</span> dans <span className="StreamCardCategory">Mathématiques</span>
              </div>
            </Link>
            </div>
          </div>
          <Link to={`/article/${this.props.id}`} className="StreamCardItemBackground"></Link>
        </article>
      </div>
    )
  }
}
