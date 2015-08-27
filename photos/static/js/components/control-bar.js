import React from 'react'
import {ButtonGroup, Button, ButtonToolbar} from 'react-bootstrap'


export const LAYOUT_THUMBNAILS = 'thumbnails';
export const LAYOUT_LIST = 'list';

export const TYPE_COLOR = 'color';
export const TYPE_BW = 'bw';
export const TYPE_ALL = 'all';


export const ControlBar = React.createClass({

  onPhotoTypeChange(photoType) {
    this.props.onPhotoTypeChange(photoType);
  },

  onLayoutChange(layout) {
    this.props.onLayoutChange(layout);
  },

  render() {
    return (
      <ButtonToolbar>
        <ButtonGroup>
          <Button
            active={this.props.photoType === TYPE_ALL}
            onClick={this.onPhotoTypeChange.bind(this, TYPE_ALL)}>
            All
          </Button>
          <Button
            active={this.props.photoType === TYPE_COLOR}
            onClick={this.onPhotoTypeChange.bind(this, TYPE_COLOR)}>
            Color
          </Button>
          <Button
            active={this.props.photoType === TYPE_BW}
            onClick={this.onPhotoTypeChange.bind(this, TYPE_BW)}>
            Black &amp; White
          </Button>
        </ButtonGroup>
        <ButtonGroup>
          <Button
            active={this.props.layout === LAYOUT_THUMBNAILS}
            onClick={this.onLayoutChange.bind(this, LAYOUT_THUMBNAILS)}>
            Thumbnails
          </Button>
          <Button
            active={this.props.layout === LAYOUT_LIST}
            onClick={this.onLayoutChange.bind(this, LAYOUT_LIST)}>
            List
          </Button>
        </ButtonGroup>
      </ButtonToolbar>
    )
  }

});


export default ControlBar;