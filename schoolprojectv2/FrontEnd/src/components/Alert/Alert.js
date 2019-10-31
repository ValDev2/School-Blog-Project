import React, {Component} from 'react';
import Button from '@material-ui/core/Button';
import Snackbar from '@material-ui/core/Snackbar';
import IconButton from '@material-ui/core/IconButton';
import CloseIcon from '@material-ui/icons/Close';
import { withStyles } from '@material-ui/styles';
import {connect} from 'react-redux';

const styles = {}

class Alert extends Component {

  render(){
    const { classes } = this.props;
    console.log(this.props.loaded);
    return(
      <div className="Alert">
        { this.props.message !== undefined &&
          <Snackbar
            anchorOrigin={{
              vertical: 'bottom',
              horizontal: 'left',
            }}
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
  return {
    message: state.authentication.error_msg[0],
    status: state.authentication.error_status,
  }
}

export default connect(mapStateToProps)(withStyles(styles)(Alert));
