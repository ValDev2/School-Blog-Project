import React, {Component} from 'react';
import { connect } from 'react-redux';
import {authLogin} from '../../actions/authentication.js';

class Login extends Component {

  constructor(props){
    super(props);
    this.state = {
      email: "",
      password: ""
    }
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e){
    this.setState({[e.target.name]: e.target.value});
  }

  handleSubmit(e){
    e.preventDefault();
    this.props.authLogin(this.state.email, this.state.password);
  }

  render(){
    return(
      <div className="Login">
        <h1> This is a form </h1>
        <form>
          <input type="text" onChange={this.handleChange} name="email"/>
          <input type="password" onChange={this.handleChange} name="password"/>
          <input type="submit" onClick={this.handleSubmit}/>
          { this.props.isAuthenticated &&
            <p>Hello </p>
          }
        </form>
      </div>
    )
  }
}

const mapStateToProps = state => {
  console.log(state);
  return {
    token: state.authentication.token
  }
}

export default connect(mapStateToProps, {authLogin})(Login);
