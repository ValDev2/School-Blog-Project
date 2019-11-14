import React, {Component} from 'react';
import BasicArticleCreationForm from './BasicArticleCreationForm.js';

class NewArticle extends Component{
  constructor(props){
    super(props);
    this.state = {
      step: 1,
      articleTitle: "",
      articleBody: "",
    }
    this.nextStep = this.nextStep.bind(this);
    this.previousStep = this.previousStep.bind(this);
    this.handleChange = this.handleChange.bind(this);
  }

  componentDidMount(){
    //do things
  }


  nextStep(e){
    e.preventDefault();
    this.setState(st => {step: st.step++});
  }

  previousStep(e){
    e.preventDefault;
    this.setState(st => {step: st.step--});
  }

  handleChange(e){
    this.setState({[e.target.name] : e.target.value});
  }

  render(){
      switch(this.state.step){
          case 1:
              console.log("yes")
              return(
                  <BasicArticleCreationForm
                    nextStep={this.nextStep}
                    previousStep={this.previousStep}
                    handleChange={this.handleChange}
                  />
            )
          case 2:
              return(
                  <h1>Extra Infos ! </h1>
              )
          case 3:
              return(
                  <h1> Ready To publish ! </h1>
              )
          case 4:
              return(
                  <h1>Successfully published ! </h1>
              )
          default:
              return(
                    <h1>Default ! </h1>
              )
      }
  }


}


export default NewArticle;
