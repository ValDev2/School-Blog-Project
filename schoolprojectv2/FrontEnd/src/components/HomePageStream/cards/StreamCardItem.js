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
              <Link to={`/article/${this.props.post.slug}`} className="StreamLink">
                <h2 className="StreamCardItemTitle">
                  {this.props.post.title}
                </h2>
                <p className="StreamCardItemSubTitle">
                  {this.props.post.content}
                </p>
              </Link>
            </div>
            <div className="StreamCardLowerContent">
            <Link to={`/article/${this.props.post.slug}`} className="StreamLink">
              <div className="StreamCardInfo">
                <span className="StreamCardUser">{this.props.post.user_name}</span> dans <span className="StreamCardCategory">{this.props.post.category_subfield}</span>
              </div>
            </Link>
            </div>
          </div>
          <Link to={`/article/${this.props.post.slug}`} className="StreamCardItemBackground"></Link>
        </article>
      </div>
    )
  }
}
