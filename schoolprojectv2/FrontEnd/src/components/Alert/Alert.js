import React, {Component} from 'react';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import { withStyles } from '@material-ui/styles';
import {connect} from 'react-redux';

const styles = {}

class Alert extends Component {

  constructor(props){
    super(props);
    this.state = {
      isOpen: false
    };
    this.handleOpen = this.handleOpen.bind(this);
  }

  componentDidUpdate(prevProps){
    if(prevProps.message !== this.props.message){
      this.handleOpen();
    }
  }

  handleOpen(){
    console.log("RESETING TO FALSE")
    this.setState({isOpen: true});
    setTimeout(() =>{
      this.setState({isOpen: false})
    }, 4000)
  }


  render(){
    console.log(this.state.isOpen);
    const { classes } = this.props;
    return(
      <div className="Alert">
        { this.props.message !== null &&
          <Snackbar
            open={this.state.isOpen}
            anchorOrigin={{
              vertical: 'bottom',
              horizontal: 'left',
            }}
            onClose={() => this.setState({isOpen: false})}
            autoHideDuration={2000}
            ContentProps={{
              'aria-describedby': 'message-id',
            }}
            message={<span id="message-id">{this.props.message && this.props.message[0]}</span>}
            action={[
              <IconButton
                key="close"
                aria-label="close"
                color="inherit"
                className={classes.close}
              >
                <CloseIcon />
              </IconButton>,
            ]}
          />
        }

      </div>
    )
  }
}


const mapStateToProps = state => {
  if (state.authentication.error !== null){
    return {
      message: state.authentication.error_msg[0],
      status: state.authentication.error_status,
    }
  }
}

export default connect(mapStateToProps)(withStyles(styles)(Alert));
