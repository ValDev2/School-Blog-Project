import React, {Component} from 'react';
import {Link} from 'react-router-dom';
import Button from '@material-ui/core/Button';
import './css/ArticleDetails.css';
import { makeStyles } from '@material-ui/core/styles';
import { withStyles } from '@material-ui/styles';
import CommentsBox from './Comments/CommentsBox.js';


const styles = {
  button: {
    lineHeight: 0,
    padding: "10px",
    marginLeft: 0,
    fontSize: "10px",
    borderColor: "#00AEAB",
    color: "#00AEAB",
    fontWeight: "500",
    transform: "scale(1.3)"
  }
}


class ArticleDetails extends Component {
  constructor(props){
    super(props);
    this.state = {
      isCommentOpen: false
    };
    this.toogleCommentsBox = this.toogleCommentsBox.bind(this);
  }

  componentDidMount(){
    console.log("Welome to the Article Details");
  }

  toogleCommentsBox(e){
    this.setState({isCommentOpen: !this.state.isCommentOpen})
  }

  render(){
    const { classes } = this.props;
    return(
      <div className="ArticleDetails">
        <article className="Article">
          <div className="ArticleDetailsContent">
            <h1 className="ArticleDetailsTitle">
              Hey, Here is the Title !
            </h1>
            <h3 className="ArticleDetailsSubTitle">
              Here goes the subtitle !
            </h3>
            <div className="ArticleDetailsUserInfos">
              <div className="ArticleDetailsUser">
                <p className="ArticleDetailsUserName">
                  Valentin
                  <span style={{marginLeft: "10px"}}>
                    Follow
                  </span>
                </p>

              </div>
              <div className="ArticleDetailsExtraInfos">
                <p className="ArticleDetailsDate"> 23 Novembre </p>
              </div>
            </div>
            <div className="ArticleDetailsMainBackground">
              <div className="ArticleDetailsBackground"></div>
              <p className="ArticleDetailsBackgroundCredit">Credit : blabla </p>
            </div>
            <div className="ArticleDetailsTextContent">
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. In blandit auctor tellus, nec semper ligula aliquam sed. Vestibulum sit amet nisl nec nibh venenatis volutpat. Suspendisse potenti. Praesent gravida lectus eu augue hendrerit, in feugiat elit venenatis. Nunc ante risus, faucibus id libero vitae, scelerisque gravida ipsum. Integer feugiat scelerisque quam, non cursus ante. Nulla non diam id purus sollicitudin lobortis vel eu urna. Mauris egestas odio nec massa pulvinar tristique. Proin pellentesque maximus elit, a interdum diam sodales eu. Nam sit amet aliquet turpis, sed lobortis leo. Nam in mollis sapien, eget vestibulum dolor. Quisque pharetra elit libero, sed eleifend mi euismod venenatis. Nulla facilisi. Morbi tempus nibh porttitor turpis venenatis efficitur. Suspendisse felis nibh, vehicula in mi at, ultrices tempor ex. Maecenas lorem erat, luctus vitae eleifend et, blandit quis dui.
                Sed quis justo ut lorem porta fringilla. Praesent efficitur accumsan leo in interdum. Aliquam faucibus odio vel libero faucibus, at condimentum erat convallis. Morbi eu luctus tellus, eu rutrum mi. Aenean dapibus placerat libero, at convallis justo maximus vitae. Fusce eu erat feugiat, lacinia neque vitae, iaculis dolor. Nullam placerat pretium velit in pulvinar.

                Cras ac porta dui. Quisque laoreet tempor gravida. Nam accumsan rutrum blandit. In arcu lectus, gravida eget sodales nec, aliquam non sapien. Vestibulum eu eros vel ante fringilla luctus. Integer scelerisque eleifend vulputate. Etiam hendrerit tortor quis fringilla porta. Sed nulla nisl, ultrices et mi id, semper lacinia erat. Maecenas dictum commodo laoreet. Sed fringilla mollis tortor, at consectetur augue laoreet nec. Sed non dapibus ante. Cras rutrum posuere lorem aliquam facilisis.

                Fusce convallis ultrices risus ultrices consequat. Sed mattis mauris at ligula sagittis, ut blandit lectus bibendum. Nam ex odio, pretium ac posuere eget, cursus at velit. Ut eu purus vitae ex imperdiet finibus eu at dolor. Morbi venenatis lectus nec tortor mollis volutpat. Quisque congue augue sed neque tristique interdum. Quisque pharetra purus sit amet lectus cursus, quis varius massa laoreet. Aliquam at pellentesque massa. Mauris dapibus auctor massa ac aliquam. Sed efficitur auctor neque at feugiat. Maecenas sed tincidunt turpis. Phasellus molestie, metus eget luctus laoreet, mauris justo accumsan neque, a scelerisque diam diam ac neque. Nullam blandit massa at massa finibus, at sagittis sapien maximus. Duis semper augue et facilisis vestibulum. Sed convallis tellus urna, a dapibus turpis auctor id.
              </p>
            </div>
            <div className="ArticleDetailsBottom">
              <div className="ArticleDetailsTags">
                <div className="ArticleDetailsSimpleTag">
                  Mathématiques
                </div>
              </div>
              <div className="ArtileDetailsSocialInfos">
                <div className="ArticleDetailsScore">
                  <div className="ArticleDetailsLikes">
                    <i className="fab fa-gratipay"></i>
                    <span className="ArticleDetailsLikeNumber">
                      300 likes
                    </span>
                  </div>
                  <div className="ArticleDetailsSocialMedia">
                    <ul className="ArticleDetailsSocialIcons">
                      <i className="fab fa-twitter"></i>
                      <i className="fab fa-linkedin-in"></i>
                      <i className="fas fa-bookmark"></i>
                    </ul>
                  </div>
                </div>
                <div className="separator"></div>
                  <div className="ArticleFooterInfos">
                    <div className="ArticleDetailsWrittenBy">
                      <div className="ArticleDetailsWrittenByContent">
                        <p className="ArticleDetailsInfosHead">L'auteur</p>
                        <div className="ArticleDetailsInfosTitle">
                          <h2>UserName </h2>
                        </div>
                        <p className="description">J'aime faire des choses ...</p>
                      </div>
                      <div className="ArticleDetailsFollowUser">
                        <Button variant="outlined" color="primary" className={classes.button}>
                          suivre
                        </Button>
                      </div>
                    </div>
                    <div className="ArticleDetailsCategory">
                      <div className="ArticleDetailsCategoryContent">
                        <div className="ArticleDetailsInfosTitle">
                          <h2>Mathématiques</h2>
                        </div>
                        <p className="description">Equation, Functions & more ... </p>
                      </div>
                      <div className="ArticleDetailsCategorySeeMore">
                        <Button variant="outlined" color="primary" className={classes.button}>
                          More
                        </Button>
                      </div>
                    </div>
                    <div className="separator"></div>
                    <div className="ArticleDetailsComments">
                    { this.state.isCommentOpen === false ? (
                      <Button variant="outlined"
                              size="large"
                              color="primary"
                              className={classes.button}
                              onClick={() => this.toogleCommentsBox()}
                              style={{
                                width: "70%",
                                fontSize: "14px",
                                padding: "20px"
                              }}>
                        Commentaires ( 3 )
                      </Button>
                    ) : (
                      <CommentsBox />
                    )
                    }
                    </div>
                  </div>
              </div>
            </div>
          </div>
        </article>
      </div>
    )
  }
}

export default withStyles(styles)(ArticleDetails);
