import React, {Component} from 'react';
import { withAlert } from 'react-alert';
import {connect} from 'react-redux';

class Alerts extends Component{

  componentDidUpdate(prevProps){
    this.props.alert.show(this.props.error.msg.detail);
  }

  render(){
    return(
      <div className="Alert">
      </div>
    );
  }
}

const mapStateToProps = state => {
  console.log(state.errors)
  return {
    error: state.errors
  }
}


export default connect(mapStateToProps)(withAlert()(Alerts));
