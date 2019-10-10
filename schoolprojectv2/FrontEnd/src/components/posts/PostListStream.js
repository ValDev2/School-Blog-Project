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
    this.sortByLikeNumber = this.sortByLikeNumber.bind(this);
  }


  componentDidMount(){
    //Getting subcategories
    this.props.getCategoryFields(this.props.field);
    //getting the most pupular posts of each subcategories
  }

  //Sort all the articles from a Category_Type by their like number
  sortByLikeNumber(){
    let result = [];
    //getting all the objects from a subclass
    this.props.categoryFields.map( field => {
      if(field.related_posts.length != 0){
        field.related_posts.map( post => result.push(post));
      }
    });
    //sorting the objects by their like_number
    result.sort( (a,b) => b.like_number - a.like_number);
    return result;
  }

  render(){
    return(
      <div className="PostListStream">
        <section className="PostList-last-stream">
          <LargeCard {...this.sortByLikeNumber()[0]}/>
          <div className="small-card-wrapper">
            <div className="small-card-content">
              <SmallCard {...this.sortByLikeNumber()[1]}/>
              <SmallCard {...this.sortByLikeNumber()[2]}/>
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
