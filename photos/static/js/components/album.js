import React from 'react'
import {Grid, Col, Row} from 'react-bootstrap'
import PhotoPanel from './photo-panel'
import FavoritePanel from './favorite-panel'


const Album = React.createClass({

  render() {

    return (
      <Grid>
        <Row>
          <Col md={10} sm={10}>
            <PhotoPanel
              photos={this.props.photos}
              favorites={this.props.favorites}/>
          </Col>
          <Col md={2} sm={2}>
            <FavoritePanel favorites={this.props.favorites}/>
          </Col>
        </Row>
      </Grid>
    )

  }

});


export default Album;