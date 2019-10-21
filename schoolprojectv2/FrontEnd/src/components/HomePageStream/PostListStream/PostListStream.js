import React, { Component } from 'react';
import { connect } from 'react-redux';
import './css/PostListStream.css';
import LargeCard from '../cards/LargeCard';
import SmallCard from '../cards/SmallCard';

class PostListStream extends Component {
  render(){
    console.log("PROPS DE PostListStream")
    console.log(this.props.posts);
    return(
      <div className="PostListStream">
        <section className="PostList-last-stream">
          <LargeCard post={this.props.posts[0]}/>
          { this.props.posts.length > 1 && (
            <div className="small-card-wrapper">
              <div className="small-card-content">
                <SmallCard post={this.props.posts[1]}/>
                <SmallCard post={this.props.posts[2]}/>
              </div>
            </div>
          )}
        </section>
        <div className="divider"></div>
      </div>
    )
  }
}

export default PostListStream;
