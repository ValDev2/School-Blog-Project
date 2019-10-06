import React, { Component } from 'react';
import { connect } from 'react-redux';
import { getCategoryFields } from '../../actions/categories';


class PostListStream extends Component {

  componentDidMount(){
    console.log("CALLING THE API TO GET THE CATFIELD");
    console.log("PROPS ? ");
    console.log(this.props);
    this.props.getCategoryFields(this.props.field);
  }

  render(){
    return(
      <div className="PostListStream">
        <h1>Hello and Welcome here ! </h1>
        <p> Page  </p>
        { this.props.categoryFields.map( field => field.related_posts.map( post => <p>{post.title}</p>))}
      </div>
    )
  }
}

const mapStateToProps = state => {
  console.log("LES STATES  de POSTLIST! ")
  console.log(state)
  return {
    categoryFields: state.categoryFields.category_fields
  }
}


export default connect(mapStateToProps, {getCategoryFields})(PostListStream);
