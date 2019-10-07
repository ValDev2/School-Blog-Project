import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getCategoryFields } from '../../actions/categories';
import './css/PostListStream.css';
import LargeCard from './cards/LargeCard';
import SmallCard from './cards/SmallCard';

class PostListStream extends Component {
  constructor(props){
    super(props);
    this.State = {
      hottestPost: []
    }
    this.getHottestPost = this.getHottestPost.bind(this);
  }



  componentDidMount(){
    //Getting subcategories
    this.props.getCategoryFields(this.props.field);
    //getting the most pupular posts of each subcategories
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

const mapStateToProps = state => {
  return {
    categoryFields: state.categoryFields.category_fields
  }
}


export default connect(mapStateToProps, {getCategoryFields})(PostListStream);
