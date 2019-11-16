import React, {Component} from 'react';
import BasicArticleCreationForm from './BasicArticleCreationForm/BasicArticleCreationForm.js';
import ExtraInfosArticleCreationForm from './ExtraInfosArticleCreationForm/ExtraInfosArticleCreationForm.js';



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
    console.log("STEP : " + this.state.step);
  }

  nextStep(e){
    this.setState({step: this.state.step+1});
  }

  previousStep(e){
    this.setState({step: this.state.step-1});
  }

  handleChange(e){
    this.setState({[e.target.name] : e.target.value});
  }

  render(){
    console.log("step : " + this.state.step);
      switch(this.state.step){
          case 1:
              return(
                  <BasicArticleCreationForm
                    nextStep={this.nextStep}
                    previousStep={this.previousStep}
                    handleChange={this.handleChange}
                  />
            )
          case 2:
              return(
                  <ExtraInfosArticleCreationForm
                    nextStep={this.nextStep}
                    previousStep={this.previousStep}
                    handleChange={this.handleChange}
                  />
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
