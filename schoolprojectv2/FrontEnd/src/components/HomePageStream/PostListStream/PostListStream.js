import React, { Component } from 'react';
import { connect } from 'react-redux';
import './css/PostListStream.css';
import LargeCard from '../cards/LargeCard';
import SmallCard from '../cards/SmallCard';

class PostListStream extends Component {

  componentDidMount(){
  }

  render(){
    return(
      <div className="PostListStream">
        <section className="PostList-last-stream">
          <LargeCard />
          <div className="small-card-wrapper">
            <div className="small-card-content">
              <SmallCard />
              <SmallCard />
            </div>
          </div>
        </section>
        <div className="divider"></div>
      </div>
    )
  }
}

export default PostListStream;
